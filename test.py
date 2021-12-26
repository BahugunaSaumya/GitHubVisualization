from github import Github
import sys
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

deadline = datetime.combine(
    date.today() + relativedelta(months=-2), 
    datetime.min.time()
)
def Average(lst):
    return sum(lst) / len(lst)
 
g= Github("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")
#name= input("name:")
usr = g.get_user(sys.argv[1])
rep=usr.get_repos()
a=[]
count=0
contk=0
for repw in rep:
  count=count+1
  print(count)
  print(repw)
  d=repw.stargazers_count
  print(repw.stargazers_count)
  a.append(d)
  

  
  print(list(repw.get_branches()))
  #print(len(list(repw.get_branches()))) 
  b= repw.get_branches()
  for t in b:
    if repw.get_commit(t.name).commit.author.date > deadline :
     print("commits for "+ str(t.name)+ " " +str(repw.get_commits(t.name).totalCount) )
  else:
    print("no latest commits")
  open_issues = repw.get_issues(state='open')
  print(list(repw.get_labels()))
  for issue in open_issues:
     print(issue)
     contk=contk+1
if usr.login is not None:
 print("user:" + usr.login)
if usr.name is not None:
 print("fullname: " +usr.name)
if usr.location is not None:
  print("location: " +usr.location)
if usr.company is not None:
  print("company: " +usr.company)
print(usr.bio)    
print(usr.tes)  
print(Average(a))  
print(count)
print("issues:"+str(contk))