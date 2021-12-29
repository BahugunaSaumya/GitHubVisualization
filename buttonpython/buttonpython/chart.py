import plotly.express as px
import pymongo
import pprint 
import os
# Loading the data
 
import pandas as pd
from pymongo.common import MAX_CONNECTING 
def main():
 conn = "mongodb://localhost:27017"    
 client = pymongo.MongoClient(conn)

# Create a database
 db = client.classDB
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
 #os.chdir("../")
 #print(os.getcwd())
 #df = pd.read_csv("..//data.csv") 
 df = pd.read_csv("data.csv")   
 #mct = db.githubuser.find({'login': {'$exists': True}})
# Creating the bar chart
 #df=[]
 #c=0
 
 """for d in mct:
     del d['_id']
     b=list(d.keys())
     
     
     df.append(d)
 for d in df:
          if d.get('company') is None :
           d['company'] = 'BASE'  
          if d.get('fullname') is None :
           d['fullname'] = 'FULLNAME'   
    fig = px.scatter(df, x='total_commits', y="followers", color='login',
                 symbol='open_issues', size='closed_issues', facet_row='average_stars',
                 facet_col='location')"""
 pprint.pprint(df)
# showing the plot
# fig = px.pie(df, values="average_stars", names='fullname')
 #fig.show()
 fig =px.scatter(df, x="total_commits", y="average_stars",
           size="followers", color="login", hover_name="company",)

# Watch as bars chart population changes
 #fig=px.bar(df, x="total_commits", y="average_stars", color="fullname",
 #animation_frame="followers", animation_group="company") 
 fig.show()
if __name__ == "__main__":
   main()