import requests
from bs4 import BeautifulSoup

def get_tweet_links(query, nitter_instance='https://nitter.net', max_tweets=100):
    url = f"{nitter_instance}/search?f=tweets&q={query}&since=&until=&near="
    tweet_links = []

    while len(tweet_links) < max_tweets:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        # print(response.content)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        links = [a['href'] for a in soup.find_all('a', href=True)]

        for link in links:
            print(link)
        tweet_elements = soup.find_all('div', class_='timeline-item')
        print(tweet_elements)

    
        for tweet_element in tweet_elements:
            tweet_link_element = tweet_element.find('a', class_='tweet-link')
            print(tweet_link_element)
            tweet_link = f"{nitter_instance}{tweet_link_element['href']}"
            tweet_links.append(tweet_link)
            if len(tweet_links) >= max_tweets:
                break

        next_page_link = soup.find('a', class_='pagination-btn')
        if next_page_link:
            url = f"{nitter_instance}{next_page_link['href']}"
        else:
            break

    return tweet_links

query = "#BTC"
tweet_links = get_tweet_links(query)

for idx, tweet_link in enumerate(tweet_links, start=1):
    print(f"{idx}. {tweet_link}")
