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
import config as con
faker  = Faker()
deadline = datetime.combine(
    date.today() + relativedelta(months=-2), 
    datetime.min.time()
)
def Average(lst):
    return sum(lst) / len(lst)

tk = os.getenv('GITHUB_PAT')
print(con.GITHUB_TOKEN)
g= Github(con.GITHUB_TOKEN)
#name= input("name:")
print(g.get_rate_limit())
usr = g.get_user(sys.argv[1])

#print(f.totalCount)
from collections import defaultdict

names=defaultdict(faker.name)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB

def printer(usr):
  log = {}
  rep=usr.get_repos()
  a=[]
  l=[]
  size=[]
  
  c=0
  count=0
  contk=0
  contc=0
  for repw in rep:
    temp={}  
    #print("repo_commits"+str(repw.get_commits().totalCount))
    temp['size']=(repw.size)
    count=count+1
    temp['fork']=repw.forks
    print(repw.get_topics())
    #print(count)
    temp['name']=repw.full_name.split('/')[1]
    #l.append(repw.full_name.split('/')[1])
   # log['repo'+str(count)]=repw["full_name"]
    print(repw.full_name)
    d=repw.stargazers_count
    #print(repw.stargazers_count)
    a.append(d)
    l.append(temp)
    
  
   # print(list(repw.get_branches()))
  #print(len(list(repw.get_branches()))) 
    
    b= repw.get_branches()
    for t in b:
      print(t.name)
      r=repw.get_commits(t.name).totalCount
      c+=r
      print("total commits="+str(r))
    #   if repw.get_commit(t.name).commit.author.date > deadline :
    #   # print("commits for "+ str(t.name)+ " " +str(repw.get_commits(t.name).totalCount) )
    #    c= c+(repw.get_commits(t.name).totalCount)
    
    #    #l.append(t)
    #    print(repw.get_commit(t.name).commit.author.date)
    log['total_commits'] = c      
    #   else:
    #  #  print("no latest commits")
    #    break
    open_issues = repw.get_issues(state='open')
    #print(list(repw.get_labels()))
    for issue in open_issues:
     #print(issue)
     contk=contk+1

    closed_issues = repw.get_issues(state='closed')
    #print(list(repw.get_labels()))
    for issu in closed_issues:
     #print(issue)
     contc=contc+1
  if not l:
    log ["repo"] =[]
  else:      
   log["repo"]=l   
  if log.get('total_commits') is None :
     log['total_commits'] =0     
  
  #print("user:" + usr.login)
  log['login']=names[usr.login].replace(" ", "") 
  if usr.name is not None: 
    print("fullname: " +usr.name)
  log['fullname']=names[usr.name]
  
   # print("location: " +usr.location)
  if usr.location is not None: 
   log['location']=usr.location.replace(",", "")
  else:
    log['location'] = 'NOVALUE'

   # print("company: " +usr.company)
  log['company']=usr.company
  #print(Average(a))
  log['average_stars']=Average(a)  
  #print(count)
  #print("issues:"+str(contk))  
  log['open_issues'] = contk
  log['closed_issues'] =contc
  if log.get('average_stars') is None :
     log['average_stars'] =0.0
  if log.get('fullname') is None :
     log['fullname'] ='NAME'  
  if log.get('average_stars') is None :
     log['average_stars'] =0.0  
  """for k, v in dict(log).items():
      
    if v is None:
      del log[k]"""
        
  f=usr.get_followers()
  fo=usr.get_following()
   
 #print(f.totalCount)
  #print(json.dumps(log))
  #log['branches']=l
  log['followers'] = f.totalCount
  log['following']=fo.totalCount
  #if log.get('_id') is not None :
   #  del log['_id']
  db.githubuser.insert_one(log)
  print(log)

printer(usr)  
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