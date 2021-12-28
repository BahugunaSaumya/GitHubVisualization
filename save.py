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
k=1
def Average(lst):
    return sum(lst) / len(lst)
tk = os.getenv('GITHUB_PAT')
g= Github("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")
#name= input("name:")
usr = g.get_user(sys.argv[1])
f=usr.get_followers().totalCount
#print(f.totalCount)
from collections import defaultdict
log = defaultdict(dict)
names=defaultdict(faker.name)

def printer(usr,log,k):
  rep=usr.get_repos()
  c=str(k)
  a=[]
  count=0
  contk=0
  for repw in rep:
    count=count+1
    #print(count)
    #log.setdefault(c, {})['repo'+str(count)]=repw["full_name"]
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
       log.setdefault(c, {})['branch'+str(count)]= repw.get_commits(t.name).totalCount
       
      else:
     #  print("no latest commits")
       log.setdefault(c, {})['commit']=0
       break
    open_issues = repw.get_issues(state='open')
    #print(list(repw.get_labels()))
    for issue in open_issues:
     #print(issue)
     contk=contk+1
      
  if usr.login is not None:
    #print("user:" + usr.login)
    log.setdefault(c, {})['login']=names[usr.login].replace(" ", "") 
  if usr.name is not None:
   # print("fullname: " +usr.name)
    log.setdefault(c, {})['fullname']=names[usr.name]
  if usr.location is not None:
   # print("location: " +usr.location)
    log.setdefault(c, {})['location']=usr.location
  if usr.company is not None:
   # print("company: " +usr.company)
    log.setdefault(c, {})['company']=usr.company
  #print(Average(a))
    log.setdefault(c, {})['average_stars']=Average(a)  
  #print(count)
  #print("issues:"+str(contk))  
    log.setdefault(c, {})['issues'] = contk
 
printer(usr,log,k)  
#print("------------------followers---------------------------------")
f=usr.get_followers()
#print(f.totalCount)
c=str(k)
log.setdefault(c, {})['followers'] = f.totalCount
for e in f:
    k=k+1
    printer(e,log,k)
   

#print(usr.bio) 
#log.setdefault(c, {})['bio'] = usr.bio  
#print(usr.raw_data)
for k, v in dict(log).items():
  for m, l in dict(v).items():
    if l is None:
        del log[m]

print (log)
  
print (log)
#return usr.raw_data
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB

db.githubuser.insert_many([log])