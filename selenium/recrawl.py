from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import time
from sympy import Id
import os, shutil
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920x1080")
# Replace the path below with the path to your Chrome WebDriver
webdriver_path = "selenium/chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path,options=chrome_options)

# Navigate to the specific tweet URL
tweet_url = "https://twitter.com/mohamad19290333/status/1644348169604440064"
driver.get(tweet_url)

# Wait for the page to load
time.sleep(5)

likes_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[4]/a/div/span/span/span")
likes_count = likes_count_element.text
print(f"The tweet has {likes_count} likes.")
quotes_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[3]/a/div/span/span/span")
quotes_count = quotes_count_element.text
print(f"The tweet has {quotes_count} quotes.")
retweets_count_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div[2]/a/div/span/span/span")
retweets_count = retweets_count_element.text
print(f"The tweet has {quotes_count} retweets.")

# Close the WebDriver
driver.quit()
