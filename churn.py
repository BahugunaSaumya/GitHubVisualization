from github import Github
from collections import defaultdict
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os
from faker import Faker 
from urllib.request import urlopen

import requests
import sys
import os
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

def printer(fil,date,count):
 _count=count  
 log = {}
 if date != 0:
    log['date']=date
 else:
   log['date']= datetime.datetime(0000,00,00,0,00,00)
 
  
 print("yes")
 if '.' in fil.get('filename'):
  log['filename']= fil.get('filename').split('.')[1]
  if fil.get('changes') == 0 :
     del log
     print("NO changes")
     return _count
  else:   
   log['changes'] = fil.get('changes')
  if fil.get('additions') == 0 :
     del log
     print("No Deletions")
     return _count
  else:   
    log['additions']= fil.get('additions')
  log['deletions']= -fil.get('deletions')
  db.githubuser.insert_one(log)
  print(log)
  print("inserted")
  print("count up :" + str(count) )
  _count+=1
  return _count  
 else:
     return _count
    
 
faker  = Faker()
deadline = datetime.combine(
    date.today() + relativedelta(months=-int(sys.argv[2])), 
    # date.today() + relativedelta(months=-sys.argv[2]), 
    datetime.min.time()
)

#def Average(lst):
#    return sum(lst) / len(lst)
count=0
tk = os.getenv('GITHUB_PAT')
g= Github("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")
usr = g.get_user(sys.argv[1])
gh_session = requests.Session()
GITHUB_USERNAME = usr.login
GITHUB_TOKEN = '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'
gh_session.auth = (GITHUB_USERNAME, GITHUB_TOKEN) 
from collections import defaultdict
names=defaultdict(faker.name)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
print(g.get_rate_limit())
db = client.classDB
rep=usr.get_repos()
for repw in rep:
 k=repw.size
 print(k)
 #b= repw.get_branches()
 c= repw.get_commits(since=deadline)
 print("commit")
 
 try:
   print(c.totalCount)
 except Exception as e:
   print(e)
   continue

 for k in c:
   print("date1= " +str(repw.get_commit(k.sha).commit.author.date ))
   if repw.get_commit(k.sha).commit.author.date > deadline :
     print("date= " +str(repw.get_commit(k.sha).commit.author.date ))
     date=repw.get_commit(k.sha).commit.author.date
     p=repw.get_commit(k.sha)
     f=p.url
     #print("url")
     #print(f)
     branch_pg = gh_session.get(url = f)
     data= branch_pg.json()
     print(date)
     fil=data['files']
     for c in range(0,len(fil)):
        #print("entered")
        count = printer(fil[c],date,count)
        if count == 101:
          sys.exit()
            #else:
             #  count+=1  
        print("count "+str(count))
   else:
      print("commit Too old")
      print(repw.get_commit(k.sha).commit.author.date)
      break


  

#return usr.raw_data
"""conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB 

db.githubuser.insert_many([log])"""