import requests
from bs4 import BeautifulSoup

def get_tweet_links(url, max_tweets):
    if(max_tweets <= 0):
        return []
    tweet_links = []
    count = 0

    while count < max_tweets:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        tweet_elements = soup.find_all('div', class_='timeline-item')
        for tweet_element in tweet_elements:
            tweet_link_element = tweet_element.find('a', class_='tweet-link')
            tweet_link = 'https://nitter.net/' + tweet_link_element['href']
            print(tweet_link)
            tweet_links.append(tweet_link)
            count += 1
            if count >= max_tweets:
                return tweet_links
                break

        next_page_link = soup.find('div', class_='show-more').find('a', href=True)['href']

        
        if next_page_link:
            url = 'https://nitter.net/search' + next_page_link
            print('---------------------------------------')
            tweet_links.append(get_tweet_links(url, max_tweets-count))
        else:
            break

    return tweet_links

url = 'https://nitter.net/search?f=tweets&q=%23BTC&since=&until=&near='
tweet_links = get_tweet_links(url, 20)

for idx, tweet_link in enumerate(tweet_links, start=1):
    print(f"{idx}. {tweet_link}")
