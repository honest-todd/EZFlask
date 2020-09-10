import tweepy as tw
import os
import csv
import datetime
from textblob import TextBlob
from config import keys

# authenicate Twitter dev credentials 
auth = tw.OAuthHandler(keys["api_key"], keys["api_secret_key"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])
api = tw.API(auth)

# retrive new data and add to data set 
def update_data( keyword, filename):

    # retrive old data
    fpath = os.path.join(keys['root_path'], 'data','{}.csv').format(filename)
    cur_data = csv.reader(open(fpath))
    for item in cur_data:
         pos = item[0]
         nue = item[1]
         neg = item[2]
    sentiment_scores = [int(pos),int(nue),int(neg)]

    # update data
    tweets = tw.Cursor(api.search,q=keyword, lang="en",since=datetime.date.today()).items(200)
    for tweet in tweets:
        t = TextBlob(str( tweet.text ))
        sentiment = t.sentiment.polarity
        if sentiment > 0:
            sentiment_scores[0]  += 1
        if sentiment < 0:
            sentiment_scores[2]  += 1
        else:
            sentiment_scores[1]  += 1  
    writer = csv.writer(open(fpath,'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['positive' , 'nuetral', 'negative'])
    writer.writerow([str(sentiment_scores[0]) , str(sentiment_scores[1]), str(sentiment_scores[2])])

    
if __name__ == '__main__':
    update_data( keys['input1'], 'data1')
    update_data( keys['input2'], 'data2')
