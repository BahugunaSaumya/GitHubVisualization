
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



  a={}
  c=0
  
  
  with open('data//data3.csv', 'w') as f:
      f.write('date,filename,changes,deletion,additions\n')
  # f.write('login,followers\n')
      mct = list(db.githubuser.find({'filename': {'$exists': True}}))
      print(mct)
      if not mct:
        return "error"
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
        print(user['date'])
        
        #user['date']=pd.to_datetime(user['date']).dt.strftime("%d %b,%Y — %I:%M %p")
       
        f.write(str(user['date'])+ ',' + str(user['filename'])+ ',' + str(user['changes'])+ ',' + str(user['deletions'])+ ',' + str(user['additions'])+'\n')
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