import requests
from bs4 import BeautifulSoup

def get_tweet_data(tweet_url):
    # Replace 'nitter.net' with the Nitter instance you want to use
    nitter_instance = 'https://nitter.net'
    nitter_tweet_url = tweet_url.replace('https://twitter.com', nitter_instance)

    response = requests.get(nitter_tweet_url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    tweet_text = soup.find('div', class_='tweet-content').text
    tweet_timestamp = soup.find('p', class_='tweet-published').text
    tweet_stats = soup.find_all('span', class_='tweet-stat')
    for tweet_stat in tweet_stats:
        icon_container = tweet_stat.find('div', class_='icon-container')

        # Get all strings (text nodes) inside the div
        text_nodes = icon_container.find_all(string=True)

        # Remove leading and trailing whitespace and filter out empty strings
        cleaned_text_nodes = [text.strip() for text in text_nodes if text.strip()]

        if cleaned_text_nodes:
            target_text = cleaned_text_nodes[0]
        else:
            target_text = "0"

        print(target_text)

    return {
        'text': tweet_text,
        'timestamp': tweet_timestamp,
    }

tweet_url = 'https://twitter.com/BWallet_Bot/status/1644336750146519040'
tweet_data = get_tweet_data(tweet_url)
print(tweet_data)
