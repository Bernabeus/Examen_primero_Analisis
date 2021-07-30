import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "hUjTftyxU1EgdnzAYyFyIsnlp"
csecret = "FnehG7j8vvmEG3rQpwFwJcY7oxyaAnjtzXsuxEA5aQ1ZY4ty3K"
atoken = "1415804186814558218-2o0qdf3t5Rg4xXWwMHofBgS7xyAaaD"
asecret = "PmoQsTa9XDueh9HBSRLkwwC336XcF6fW8hQu4IYQBaQOI"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:juan1997@localhost:5984/') 
try:
    db = server.create('examenbimestre')
except:
    db = server['examenbimestre']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-79.2461,-0.4254,-77.1648,0.6884])  
#-79.2461,-0.4254,-77.1648,0.6884
twitterStream.filter(track=['Juegos olímpicos','Tenis'])
