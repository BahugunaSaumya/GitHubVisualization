from github import Github
from collections import defaultdict
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os
from faker import Faker 
from urllib.request import urlopen
import config as con
import requests
import sys
import os
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
faker  = Faker()
deadline = datetime.combine(
    date.today() + relativedelta(months=-2), 
    datetime.min.time()
)
#def Average(lst):
#    return sum(lst) / len(lst)

tk = os.getenv('GITHUB_PAT')
g= Github(con.GITHUB_TOKEN)
usr = g.get_user(sys.argv[1])
gh_session = requests.Session()
GITHUB_USERNAME = usr.login
gh_session.auth = (GITHUB_USERNAME,con.GITHUB_TOKEN) 
#name= input("name:")
log={}

#print(f.totalCount)
from collections import defaultdict

names=defaultdict(faker.name)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
print(g.get_rate_limit())

db = client.classDB
def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
          
    return(sum) 
""" 
def printer(fil,date):
#  print(usr.events_url)
 log = {}
 if date is not 0:
    log['date']=date
 else:
   log['date']= datetime.datetime(0000,00,00,0,00,00)
 
  
  #a=[]
  #l=[]
  #c=0
  #filenam=[]
  #additions=[]
  #delw=[]
  #change=[]
  #data={}
  #count=0
  #contk=0
  #contc=0
  
    #"""#   e=repw.get_events()
    #for w in e:
    #  print(w)"""
   # count=count+1
    #print("n")
    #print(repw.get_topics())
    #print(repw.get_pull)
    #print(count)
    #log['repo'+str(count)]=repw.full_name
    #print(repw)
    #d=repw.stargazers_count
    #print(repw.star

from bson.objectid import ObjectId
rep=usr.get_repos()
for repw in rep:
    count=0
    print("reeo  :" + repw.full_name.split('/')[1])
    log['reponame']= repw.full_name.split('/')[1]
    k=repw.size
    log['reposize']= repw.size/1000
    print(k)
    b= repw.get_branches()
    for t in b:
        count+=1 
    log['branches']=count 
    log['_id'] = ObjectId()    
    db.githubuser.insert_one(log)
    print(log)
    print("inserted")
  

#print("------------------followers---------------------------------")
#f=usr.get_followers()
#print(f.totalCount)

#if f.totalCount != 0:
 #for e in f:
 
  #  printer(e)
   

#print(usr.bio) 
#log['bio'] = usr.bio  
#print(usr.raw_data)



  

#return usr.raw_data
"""conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB 

db.githubuser.insert_many([log])"""