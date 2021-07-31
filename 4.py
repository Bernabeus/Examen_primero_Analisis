from facebook_scraper import get_posts
import couchdb
import json
import time
import pymongo
import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

db_client = pymongo.MongoClient("mongodb://localhost:27017") 
Examen = db_client.Examen
my_posts = Examen.posts
    
i=1
for post in get_posts('olympics',pages=50,extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
    
    doc['id']=id
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}
        
        doc['post_url']=post['post_url']
        my_posts.save(doc)
        
        print('Guardado')
    except Exception as e:
        print('Se encontro un problema:'+str(e))
