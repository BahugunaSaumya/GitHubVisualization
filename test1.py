from pprint import pprint
from github import Github
from collections import defaultdict
import json                 # for converting a dictionary to a string
import base64
from bson.objectid import ObjectId
import github.GithubObject
import github.Repository
import pymongo              # for mongodb access
import os
from faker import Faker 
from urllib.request import urlopen

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
co=0
tk = os.getenv('GITHUB_PAT')
g= Github("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")
#name= input("name:")
usr = g.get_user(sys.argv[1])

#print(f.totalCount)
from collections import defaultdict

names=defaultdict(faker.name)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
print(g.get_rate_limit())

db = client.classDB
#def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
 #   sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
  #  for i in arr:
#         sum = sum + i
          
#    # return(sum) 
  
# def printer(usr):
#   print(usr.events_url)
log = {}
o=[]
rep=usr.get_repos()
import requests  
gh_session = requests.Session()
GITHUB_USERNAME = usr.login
GITHUB_TOKEN = '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'
gh_session.auth = (GITHUB_USERNAME, GITHUB_TOKEN) 
#def out(log,val):
   
#   a=[]
#   l=[]
#   c=0
#   filenam=[]
#   additions=[]
#   delw=[]
#   change=[]
#   data={}
#   count=0
#   contk=0
#   contc=0
for repw in rep:
 b= repw.get_branches()
 #print(repw.get_contents(""))
 log["id"]=repw.full_name
 log['datum']=repw.size
 #print(repw.full_name)
 a=[]
 for t in b:
  #print("branch = "+t.name)
  bran={}
  bran['id']=t.name
  bran["datum"]=len(repw.get_contents("",ref=t.name))
  contents=repw.get_contents("",ref=t.name)
  #print(repw.get_contents("",ref=t.name))
  while contents:
     file_content = contents.pop(0)
   #  print(file_content)
     
    # print("dir^|")
     #print("URl=" +file_content.url)
     #print("type"+file_content.type)
     if file_content.type == "dir":
        try:
         contents.extend(repw.get_contents(path=file_content.path))
        except Exception as e:
            k=[]           
            k.append(file_content.url)
            while k:
      #       print(k)
             branch_pg = gh_session.get(url = k.pop(0))
             data=branch_pg.json()
             for c in range(0,len(data)):
              if data[c].get('type') =="dir":
               k.append(data[c].get('url'))
              else:
                 file={}
                 #a.append(data[c].get('name'))
                 file["datum"]=data[c].get('size')
                 file['id']=data[c].get('name')
                 a.append(file)
       #          pprint(a )


                  
                  
                  
     else:
        # print(file_content.name)
         file={}
         file["datum"]=file_content.size
         file['id']=file_content.name
         a.append(file)
         #pprint(a)
  log['_id'] = ObjectId()        
  bran["children"]=a
  o.append(bran)   
  
 log['_id'] = ObjectId()
 log['children']=o    
 pprint(log)
 try:
  db.githubuser.insert_one(log)
 except Exception as e:
    co+=1
    print("File was too big to enter\n"+str(co)+": Missed")
    continue
print("Files Missed"+str(co))
    #  if repw.get_commit(t.name).commit.author.date > deadline :
     #  k=repw.get_commit(t.name)
      # print
      # f=k.url
       
       #data_json=urlopen(f)
       #data = json.load(data_json)
       #fil=data['files']
       #print(fil)
       #for c in range(0,len(fil)):
        #print(fil[c].get('filename').split('.')[1])
        #filenam.append(fil[c].get('filename').split('.')[1])
        #print("changes:")
        #print(fil[c].get('changes'))
        #change.append(fil[c].get('changes'))
        #additions.append(fil[c].get('additions'))
        #delw.append(fil[c].get('deletions'))
       #m=k.stats
       #print("additions:" +str(m.additions))
       #print("deletions:" +str(m.deletions))
       #print("Total"+str(m.total))
      # print("commits for "+ str(t.name)+ " " +str(repw.get_commits(t.name).totalCount) )
       #c= c+(repw.get_commits(t.name).totalCount)
       #log['total_commits'] = c
      # l.append(t.name  )
     #  print(repw.get_commit(t.name).commit.author.date)

      #else:
     #  print("no latest commits")
       #break
    #open_issues = repw.get_issues(state='open')
    #print(list(repw.get_labels()))
    #for issue in open_issues:
     #print(issue)
     #contk=contk+1

    #closed_issues = repw.get_issues(state='closed')
    #print(list(repw.get_labels()))
    #for issu in closed_issues:
     #print(issue)
#      contc=contc+1
# if log.get('total_commits') is None :
#      log['total_commits'] =0     
 
#   #print("user:" + usr.login)
# log['login']=names[usr.login].replace(" ", "") 
# if usr.name is not None: 
#     print("fullname: " +usr.name)
# log['fullname']=names[usr.name]
# log['filename']=filenam
# log['changes']=_sum(change)
# log['deletion']=-_sum(delw)
# log['addition']=_sum(additions)
#    # print("location: " +usr.location)
# if usr.location is not None: 
#    log['location']=usr.location.replace(",", "")
#   else:
#     log['location'] = 'NOVALUE'
#   print(count) 
#    # print("company: " +usr.company)
#   log['company']=usr.company
#   #print(Average(a))
#   log['average_stars']=Average(a)  
#   #print(count)
#   #print("issues:"+str(contk))  
#   log['open_issues'] = contk
#   log['closed_issues'] =contc
#   if log.get('average_stars') is None :
#      log['average_stars'] =0.0
#   if log.get('fullname') is None :
#      log['fullname'] ='NAME'  
#   if log.get('average_stars') is None :
#      log['average_stars'] =0.0  
#   if len(log.get('filename')) is 0 :
#      log['filename']= ['empty'] 
#   if log.get('changes') is 0 :
#      log['changes']=0
#   if log.get('deletion') is 0 : 
#      log['deletion']=0
#   if log.get('addition') is 0 :
#      log['addition']=0          
#   """for k, v in dict(log).items():
      
#     if v is None:
#       del log[k]"""
        
#   f=usr.get_followers()
#  #print(f.totalCount)
#   #print(json.dumps(log))
#   log['branches']=l
#   log['followers'] = f.totalCount
#   #if log.get('_id') is not None :
#    #  del log['_id']
#   db.githubuser.insert_one(log)
#   print(log)

# printer(usr)  
# #print("------------------followers---------------------------------")
# f=usr.get_followers()
# #print(f.totalCount)

# if f.totalCount != 0:
#  for e in f:
 
#     printer(e)
   

#print(usr.bio) 
#log['bio'] = usr.bio  
#print(usr.raw_data)



  

#return usr.raw_data
"""conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.classDB 

db.githubuser.insert_many([log])"""