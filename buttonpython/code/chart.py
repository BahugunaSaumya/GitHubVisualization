import plotly.express as px
import plotly.graph_objects as go
import pymongo
import pprint 

import os
import numpy as np
import matplotlib.pyplot as plt

# Loading the data
from pandas.api.types import CategoricalDtype
import sys
 
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

 print(os.getcwd())
 #sys.path.append('D:\\study\\GitHubVisualization\\buttonpython\\buttonpython')
 #df = pd.read_csv("..//data.csv") 
 df = pd.read_csv("data//data3.csv")   
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
 """fig =px.scatter(df, x="total_commits", y="average_stars",
           size="followers", color="login", hover_name="company",)
 """
 """colors = ['blue', 'green', 'black', 'purple', 'red', 'brown']
 # Watch as bars chart population changes
  #fig=px.bar(df, x="total_commits", y="average_stars", color="fullname",
  #animation_frame="followers", animation_group="company") 
  #fig.write_html("./template/file.html")
 fig = px.pie(df,labels='filename', values='changes', names='filename', title='Code churn')
 fig.update_traces(hoverinfo='label+percent', textfont_size=20,
                   pull=[0.1, 0, 0.2, 0, 0, 0],
                  marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2)))
 fig.show()
 """
 fig = go.Figure()
 fig.add_trace(go.Bar(x=df['filename'], y=df['additions'], name='additions',  
            #base=0,
            hovertext=df['date']
           ))
 fig.add_trace(go.Bar(x=df['filename'], y=df['deletion'], name='deletion', 
           hovertext=df['date']
           #base=0,
           #width=0.5
          ))

 #"""
 #
 # 
 # making a dataset for churning
 # 
 # 
 # 
 #          
 #with open('data5.csv', 'w') as f:
 #     f.write('date,addition,deletion,churn\n')
  # f.write('login,followers\n')

 df['date'] = pd.to_datetime(df['date']) - pd.to_timedelta(7, unit='d')
 df = df.groupby([pd.Grouper(key='date', freq='W-MON')])['additions' , 'deletion'].sum().reset_index().sort_values('date')

#dt = df.groupby([pd.Grouper(key='date', freq='W-MON')])['deletion'].sum().reset_index().sort_values('date')
 df['churn']=(-df['deletion']/df['additions'])*100
      #for d in df:
       
     # f.write( ','+ str(df['additions'])+ ',' + str(df['deletion']) + ',' + str(df['churn']))
 #dm=
 df.reset_index(drop=True)
 print(df)
 fig1=px.scatter(df, x="date", y="churn",
                 hover_data=['churn'])

 fig2=px.line(df,x="date",y="churn")
 fig2.update_traces(line=dict(color = 'red'),opacity=1)
 fig4 = go.Figure(data=fig1.data + fig2.data)

 fig4.update_layout(
    title="Churn Rate",
    xaxis_title="Date",
    yaxis_title="Churn Rate in '%",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
 fig.update_layout(
    title="Churn Visualization",
    xaxis_title="Filename",
    yaxis_title="Addition(>0)_Deletion(<0)",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
    #    size=18,
        color="RebeccaPurple"
    )
)
#fig1 = px.line(df, x="date", y="churn", color='churn',trendline="ols")
 print (df)

#fig.update_traces(textposition='inside', textfont_size=1)
#layout = go.Layout(
 #   barmode='stack',
#)

#from plotly.offline import init_notebook_mode, iplot
#fig = dict(data = data, layout = layout)
#iplot(fig, show_link=False)
 #fig.show()
 fig.write_html("D:\\study\\GitHubVisualization\\buttonpython\\template\\Churn_bar.html")
 #fig4.show()
 fig4.write_html("D:\\study\\GitHubVisualization\\buttonpython\\template\\Churn_Rate.html")


if __name__ == "__main__":
   main()