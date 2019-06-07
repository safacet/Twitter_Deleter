# You need to download your twitter archive and change the tweet.js file to cvs file
# You should enter your consumer key/secret and access key/secret
# And off course youu need to enter your files destination on the code



import tweepy
import csv
import re

consumer_key = 'here'
consumer_secret = 'here'
access_key = 'here'
access_secret = 'here'

def read_csv(file):
    """
    reads a CSV file into a list of lists
    """
    with open(file, encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rows = []
        for line in reader:
            for element in line:
                if ('\"id\" :' in element):
                    rows.append(element)
    return(rows)




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print("Authenticated as: %s" % api.me().screen_name)



tweets = read_csv('tweet.cvs file ')

tweets_marked = []
count = 0
for tweet in tweets:
    count += 1
    if (count > 50):
        tweets_marked.append(re.findall("\d+",tweet))



delete_count = 0

for element in tweets_marked:
    for integersid in element:
        try:
            api.destroy_status(integersid)
            print(integersid, 'deleted!')
            delete_count += 1
        except:
            print(integersid, 'could not be deleted.')
        print(delete_count, 'tweets deleted.')

