from github import Github
from collections import defaultdict
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os
from faker import Faker 


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

def Average(lst):
    return sum(lst) / len(lst)
tk = os.getenv('GITHUB_PAT')
g= Github("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")
#name= input("name:")
usr = g.get_user(sys.argv[1])

#print(f.totalCount)
from collections import defaultdict
log = {}
names=defaultdict(faker.name)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB
def printer(usr):
  rep=usr.get_repos()
  a=[]
  c=0
  count=0
  contk=0
  for repw in rep:
    count=count+1
    #print(count)
   # log['repo'+str(count)]=repw["full_name"]
    #print(repw)
    d=repw.stargazers_count
    #print(repw.stargazers_count)
    a.append(d)
  

  
   # print(list(repw.get_branches()))
  #print(len(list(repw.get_branches()))) 
    b= repw.get_branches()
    for t in b:
      if repw.get_commit(t.name).commit.author.date > deadline :
      # print("commits for "+ str(t.name)+ " " +str(repw.get_commits(t.name).totalCount) )
       c= c+(repw.get_commits(t.name).totalCount)
       log['total_commits'] = c
      else:
     #  print("no latest commits")
       log['commit']=0
       break
    open_issues = repw.get_issues(state='open')
    #print(list(repw.get_labels()))
    for issue in open_issues:
     #print(issue)
     contk=contk+1
      
  if usr.login is not None:
    #print("user:" + usr.login)
    log['login']=names[usr.login].replace(" ", "") 
  if usr.name is not None:
   # print("fullname: " +usr.name)
    log['fullname']=names[usr.name]
  if usr.location is not None:
   # print("location: " +usr.location)
    log['location']=usr.location
  if usr.company is not None:
   # print("company: " +usr.company)
    log['company']=usr.company
  #print(Average(a))
    log['average_stars']=Average(a)  
  #print(count)
  #print("issues:"+str(contk))  
    log['issues'] = contk
    
    for k, v in dict(log).items():
      if v is None:
        del log[k]
  f=usr.get_followers()
 #print(f.totalCount)
  print(log)

  log['followers'] = f.totalCount
  db.githubuser.insert_many([log])

printer(usr)  
#print("------------------followers---------------------------------")
f=usr.get_followers()
#print(f.totalCount)

log['followers'] = f.totalCount
if f.totalCount != 0:
 for e in f:
 
    printer(e)
   

#print(usr.bio) 
#log['bio'] = usr.bio  
#print(usr.raw_data)



  

#return usr.raw_data
"""conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB

db.githubuser.insert_many([log])"""