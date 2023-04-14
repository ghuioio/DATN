import pandas as pd

# Load the CSV file
data = pd.read_csv('100coin100tweets.csv', encoding='utf-8')

# Normalize the attributes
normalized_data = data.copy()
normalized_data['followersCount'] = data['followerCount'] / data['followerCount'].max()
normalized_data['likeCount'] = data['likeCount'] / data['likeCount'].max()
normalized_data['quoteCount'] = data['quoteCount'] / data['quoteCount'].max()
normalized_data['replyCount'] = data['replyCount'] / data['replyCount'].max()
normalized_data['retweetCount'] = data['retweetCount'] / data['retweetCount'].max()

# Assign weights to the attributes
weights = {
    'followerCount': 0.5,
    'likeCount': 0.3,
    'quoteCount': 0.05,
    'replyCount': 0.05,
    'retweetCount': 0.1
}

# Calculate the score
normalized_data['score'] = (normalized_data['followersCount'] * weights['followersCount'] +
                            normalized_data['likeCount'] * weights['likeCount'] +
                            normalized_data['quoteCount'] * weights['quoteCount'] +
                            normalized_data['replyCount'] * weights['replyCount'] +
                            normalized_data['retweetCount'] * weights['retweetCount'])

# Sort tweets by the score
sorted_data = normalized_data.sort_values(by='score', ascending=False)

# Display the top-ranked tweets
print(sorted_data.head(10))
