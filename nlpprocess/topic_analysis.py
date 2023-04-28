import csv
import re
import gensim
import gensim.corpora as corpora
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

# Load the tweets from the CSV file
tweets = []
with open('100coin1000tweets.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for i, row in enumerate(csv_reader):
        # if i >= 1000:  # Break the loop after reading 1000 rows
        #     break
        tweets.append(row[4])  # Append the tweet content

# Now, the `tweets` list contains the first 1000 tweets from the CSV file
print(f"Number of tweets read: {len(tweets)}")

# Preprocess the tweets
def preprocess(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'#\w+', '', text)  # Remove hashtags
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert text to lowercase

    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

processed_tweets = [preprocess(tweet) for tweet in tweets]

# Create the dictionary and corpus for LDA
dictionary = corpora.Dictionary(processed_tweets)
corpus = [dictionary.doc2bow(tweet) for tweet in processed_tweets]

# Train the LDA model
num_topics = 5
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# Display the top keywords for each topic
keywords_per_topic = 10
for topic_id in range(num_topics):
    keywords = lda_model.show_topic(topic_id, keywords_per_topic)
    print(f"Topic {topic_id + 1}:")
    for keyword, weight in keywords:
        print(f"  {keyword} ({weight:.4f})")
    print()
