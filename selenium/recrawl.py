from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import time
from sympy import Id
from selenium.common.exceptions import NoSuchElementException
import os, shutil
import snscrape.modules.twitter as sntwitter
import sys
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920x1080")
# Replace the path below with the path to your Chrome WebDriver
webdriver_path = "selenium/chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path,options=chrome_options)

def recrawl(tweet_url):
    # Navigate to the specific tweet URL
    # tweet_url = "https://twitter.com/mohamad19290333/status/1644348169604440064"
    driver.get(tweet_url)
    # Wait for the page to load
    time.sleep(5)
    try:
        retweets_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[2]/a/div/span/span/span")
        retweets_count = retweets_count_element.text if retweets_count_element else 0
    except NoSuchElementException:
        retweets_count = 0
    print(f"The tweet has {retweets_count} retweets.")
    try:
        quotes_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[3]/a/div/span/span/span")
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

# Function to get the username from a tweet URL
def extract_username_from_url(url):
    username = url.split('/')[3]
    return username

# Function to get the follower count of a user
def get_follower_count(username):
    user = sntwitter.TwitterSearchScraper('from:{}'.format(username)).get_items()
    print(user)

# Main function
if __name__ == "__main__":
    # Replace this example URL with the actual tweet URL
    tweet_url = "https://twitter.com/traderistanbul/status/1644341183215181829"
    username = extract_username_from_url(tweet_url)
    print(username)
    get_follower_count(username)



