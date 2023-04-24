from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import time
from sympy import Id
from selenium.common.exceptions import NoSuchElementException
import os, shutil
import snscrape.modules.twitter as sntwitter
import sys, json
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920x1080")
# Replace the path below with the path to your Chrome WebDriver
webdriver_path = "selenium/chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path,options=chrome_options)

def recrawl(tweet_url):
    # tweet_url = "https://twitter.com/mohamad19290333/status/1644348169604440064"
    driver.get(tweet_url)
    time.sleep(5)
    try:
        retweets_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[2]/a/div/span/span/span")
        retweets_count = retweets_count_element.text if retweets_count_element else 0
    except NoSuchElementException:
        retweets_count = 0
    print(f"The tweet has {retweets_count} retweets.")
    try:
        quotes_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[2]/a/div/span/span/span")
        quotes_count = quotes_count_element.text if quotes_count_element else 0
    except NoSuchElementException:
        quotes_count = 0
    print(f"The tweet has {quotes_count} quotes.")
    try: 
        likes_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[4]/a/div/span/span/span")
        likes_count = likes_count_element.text if likes_count_element else 0
    except NoSuchElementException:
        likes_count = 0
    print(f"The tweet has {likes_count} likes.")
    
    # Close the WebDriver
    driver.quit()
    return likes_count, quotes_count, retweets_count

def extract_profile_url(tweet_url):
    parts = tweet_url.split('/')
    if len(parts) >= 4:
        return f"https://{parts[2]}/{parts[3]}"
    else:
        return None
    
def get_user_data(tweet_url):
    username = tweet_url.split('/')[3]
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(username).get_items()):
        print(tweet.user.url)
        if tweet.user.url == extract_profile_url(tweet_url):
            return tweet.user.followersCount
            break 

# Main function
if __name__ == "__main__":
    print(recrawl('https://twitter.com/hxD9585/status/1649323527252877312'))



