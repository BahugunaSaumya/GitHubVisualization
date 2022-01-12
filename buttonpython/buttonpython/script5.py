
import pymongo              # for mongodb access
import pprint 
import json
import pandas as pd
# a script to do python based access to the mongodb
# step 6 - Let's do a useful search
def main():
  print("Demonstration python based mongodb access")

              # for pretty printing db data

# Let's get the user object from the db

# Establish connection
  conn = "mongodb://localhost:27017"
  client = pymongo.MongoClient(conn)

# Create a database
  db = client.classDB


# now that we have data we want to generate an output that works for a visualisation
# I'm going to generate a simple bar chart that shows a count of public repos of each
# user in the database. Note that this isn't a great example of a visualisation of
# inteeresting data, but it's good enough for the purpose of demonstrating how to
# complete the link between data gathering and data visualisation.

# First let's describe the data structure our visualisation needs. Look to index.html
# for the code that uses it.

# I've previously discussed the use of json data and i recommend generating and transmitting data in json format.
# However because this example is so simple, I'm goign to write the data set out in csv format
# It will look like this:
#           User, Repo Count
#           Ben,12
#           Bill,2
#           Jack,34
#           Jill 50

  a={}
  c=0
  
  """ with open('data1.csv', 'w') as m:
      m.write('total_commits,average_stars\n')
  # f.write('login,followers\n')
      dct = db.githubuser.find({'login': {'$exists': True}})
      for user in dct:
        #c=c+1
       
        del user['_id']
        b=list(user.keys())
        #pprint.pprint(json.dumps(user))
        b=list(user.keys())
       # print()
        
        m.write(str(user['total_commits']) + ',' + str(user['followers'])+'\n')"""
  with open('circles.csv', 'w') as f:
      f.write('id,datum,children\n')
  # f.write('login,followers\n')
      mct = list(db.githubuser.find({'reponame': {'$exists': True}}))
      print(mct)
      """ for m in mct:
        del m['_id']
        for k,v in m.items():
         
            
         print(str(k) +':'+str(v))
       """
      for user in mct:
        #c=c+1
        """if user.get('company') is None :
           user['company'] = 'BASE'  
        if user.get('fullname') is None :
           user['fullname'] = 'FULLNAME'""" 
        del user['_id']
        b=list(user.keys())
        #pprint.pprint(json.dumps(user))
        print(b)
       # print()
       # a[user['login']]=user
        print(user)
       # print(user['date'])
        
        #user['date']=pd.to_datetime(user['date']).dt.strftime("%d %b,%Y — %I:%M %p")
        for a in range(0,len(user['files'])): 
         f.write(str(user['reponame'])+ ',' + str(user['branch'])+ ',' + str(user['files'][a].get('filename'))+'\n')
  #print(a)
  return mct 
  
         # str(user['branches'])+ str(user['filename'])+
    
    

if __name__ == "__main__":
   main()
"""def exc():
  conn = "mongodb://localhost:27017"
  client = pymongo.MongoClient(conn)

# Create a database
  db = client.classDB
  dct = db.githubuser.find({'login': {'$exists': True}})
  with open('data.csv', 'w') as f:
      f.write('total_commits,login,fullname,location,followers,company,average_stars,open_issues,closed_issues')
  # f.write('login,followers\n')
   
      for user in dct:
        #c=c+1
       
        del user['_id']
        b=list(user.keys())
       # pprint.pprint(json.dumps(user))
        b=list(user.keys())
       # print()
      #  a[user['login']]=user
         
        
        f.write('\n') 
        for c in b:
             f.write(str(user[c]) + ',')
      #       print()
  """