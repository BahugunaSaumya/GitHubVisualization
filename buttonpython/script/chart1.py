import plotly.express as px
import plotly.graph_objects as go
import pymongo
import pprint 

import os
import numpy as np


# Loading the data
from pandas.api.types import CategoricalDtype

 
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
df = pd.read_csv("data//data4.csv")   
 #mct = db.githubuser.find({'login': {'$exists': True}})
# Creating the bar chart
 #df=[]
 #c=0
 
 
fig = px.scatter(df, y='branches', x="reponame", color= 'reponame',
                size='reposize')
pprint.pprint(df)
fig2=px.line(df,x='reponame',y='branches')
fig2.update_traces(line=dict(color = 'rgba(50,50,50,0.2)'))
fig4 = go.Figure(data=fig.data + fig2.data)
        
#fig.update_traces(textposition='inside', textfont_size=1)
#layout = go.Layout(
 #   barmode='stack',
#)
fig4.update_layout(
    autosize=True,
    width=1900,
    height=1000,
    
    #paper_bgcolor="LightSteelBlue",
)
fig4.update_xaxes(automargin=True)
fig4.update_yaxes(automargin=True)
#from plotly.offline import init_notebook_mode, iplot
#fig = dict(data = data, layout = layout)
#iplot(fig, show_link=False)
fig4.write_html("template//compare_graph.html")
print("done")
# bins represent the number of bars to make
# Can define x label, color, title
# marginal creates another plot (violin, box, rug)


# Define hover info, text size, pull amount for each pie slice, and stroke


if __name__ == "__main__":
   main()