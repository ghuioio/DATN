import snscrape.modules.twitter as sntwitter
import csv
import os

coinList = ['BTC','ETH','USDT', 'BNB','USDC','XRP', 'ADA', 'DOGE', 'STETH', 'MATIC',
            'SOL', 'DOT', 'BUSD', 'LTC', 'SHIB', 'TRX','AVAX', 'DAI', 'UNI', 'WBTC',
            'LINK','TON','ATOM','LEO','ETC','XMR','XLM','OKB','BCH','FIL',
            'LDO','TUSD','APT','HBAR','QNT','VET','CRO','NEAR','ALGO','APE',
            'ARB','ICP','EOS','FTM','GRT','SAND','AAVE','MANA','STX','THETA',
            'FRAX','EGLD','FLOW','XTZ','EDGT','AXS','IMX','RPL','NEO',
            'KCS','CRV','USDP','CFX', 'KLAY','BIT','LUNC','GT','USDD','WBT'
            'OP','BSV','CAKE','FXS','CHZ','GMX','MINA','MIOTA','MKR','DASH',
            'XEC','BTT','HT','BGB','XDC','CETH','KAS','TKX','PAXG','TWT',
            'XAUT','XRD','AGIX','CUSDC','ZIL','ENJ','RNDR','RUNE','INJ','RETH'
            ]  
# Set the query parameters
max_tweets = 1


# Open a CSV file to store the tweets
with open('100coin1tweets.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["name","id", "url", "date", "content", "userId", "followerCount", "likeCount", "quoteCount", "replyCount", "retweetCount"])

    for coinname in coinList:   
        query = '#' + coinname
        # Scrape the tweets
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= max_tweets:
                break

            # Write the specified attributes to the CSV file
            csv_writer.writerow([coinname, tweet.id, tweet.url, tweet.date, tweet.rawContent, tweet.user.url, tweet.user.followersCount, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount])
            # print([coinname, tweet.id, tweet.url, tweet.date, tweet.rawContent, tweet.user.url, tweet.user.followersCount, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount])

        print("Done " + coinname)

print("Tweets have been successfully scraped and saved to btc_tweets.csv")
