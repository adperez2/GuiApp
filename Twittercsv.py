import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "covid"
tweets = []
limit = 200

for tweet in sntwitter.TwitterSearchScraper.get_items():
    print(vars(tweet))
    if len(tweets) == limit: break
    else:

        tweets.append ([tweet.date, tweet.content])

    df = pd.DataFrame(tweets, columns["Date", "Content"])
    print(df)

df.to_csv("Csumb.csv")

