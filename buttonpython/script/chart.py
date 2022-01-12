from matplotlib import colorbar, legend
import plotly.express as px
import plotly.graph_objects as go
import pymongo
import pprint
import os
import sys

sys.path.append('..//')
print(os.getcwd())


import numpy as np
import matplotlib.pyplot as plt

# Loading the data
from pandas.api.types import CategoricalDtype

#sys.path.append(BASE_DIR)
 
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
 di=df
 dl=df
 print(os.getcwd())
 di=di.groupby("filename")['additions','deletion'].sum().reset_index().sort_values('filename') 
 fig = go.Figure()
 print(di['additions'])
 fig.add_trace(go.Bar(x=di['filename'], y=di['additions'], name='additions',  
            base=0,
            hovertext=di['additions'],marker_color=" #a569bd "
           ))
 fig.add_trace(go.Bar(x=di['filename'], y=di['deletion'], name='deletion', 
           hovertext=df['deletion'],marker_color=' #1c2833',
           base=max(df['deletion']),
           #width=0.5
          ))
 fig.update_layout(barmode='stack')         
 fig3 = go.Figure()
 dl=dl.groupby("filename")['changes'].sum().reset_index().sort_values('filename') 
 fig3.add_trace(go.Bar(x=dl['filename'], y=dl['changes'], name='change',  
            #base=0,
            marker_color="lightpink",
            hovertext=dl['changes']
           ))
 fig3.update_layout(
    title="Total Change",
    xaxis_title="Filename",
    yaxis_title="Total Change",)
 fig3.write_html("template\\changes.html")
 print("shown")
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
#  fig1=px.scatter(df, x="date", y="churn",
#                  hover_data=['churn'])

#  fig2=px.line(df,x="date",y="churn")
#  fig2.update_traces(line=dict(color = 'red'))
#  fig4 = go.Figure(data=fig1.data + fig2.data)
 #fig5 = px.line(df, x="date", y="churn",hover_data=['churn'],markers=True)
 fig5 = go.Figure(data=go.Scatter(x=df['date'], y=df["churn"]))
 fig5.update_traces(mode = 'lines+markers')
 fig5.update_layout(
    title="Churn Rate",
    xaxis_title="Date",
    yaxis_title="Churn Rate in '%",
  
    
)
 fig.update_layout(
    title="Churn Visualization",
    xaxis_title="Filename",
    yaxis_title="Addition(>0)_Deletion(<0)",
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
 fig.write_html("template\\Churn_bar.html")
 #fig4.show()
 fig5.write_html("template\\Churn_Rate.html")


if __name__ == "__main__":
   main()