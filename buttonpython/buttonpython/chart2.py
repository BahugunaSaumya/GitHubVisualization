
import circlify
import matplotlib.pyplot as plt # this is just to demonstrate with matplotlib
import plotly.graph_objects as go
import pandas as pd

import pymongo              # for mongodb access
import pprint 
import json
import pandas as pd
# a script to do python based access to the mongodb
# step 6 - Let's do a useful search
#def main():
 # print("Demonstration python based mongodb access")

              # for pretty printing db data

# Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.classDB
with open('circles.csv', 'w') as f:
 f.write('x,y,label\n')
 mct = list(db.githubuser.find({'id': {'$exists': True}}))
 #print(mct)
 """ for m in mct:
     del m['_id']
        for k,v in m.items():
         
            
         print(str(k) +':'+str(v))
       """
 #for user in mct:  
 # compute circle positions:
 circles = circlify.circlify(
    mct, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
 )

 # create some child circles based on same magnitudes above and using the circle x, y, and r calculated above


 fig = go.Figure() 

# Set axes properties
 fig.update_xaxes(
    range=[-1.05, 1.05], # making slightly wider axes than -1 to 1 so no edge of circles cut-off
    showticklabels=False,
    showgrid=False,
    zeroline=False
 )

 fig.update_yaxes(
    range=[-1.05, 1.05],
    showticklabels=False,
    showgrid=False,
    zeroline=False,
 )
 #print(df)
 # add parent circles
 from random import randint
 colors=[]
 for i in range(10):
    colors.append('#%06X' % randint(0, 0xFFFFFF))      
 def center(x1, x2, y1, y2) :
  
    x=(x1 + x2) / 2
    y=(y1 + y2) / 2 
    return x,y
 # Driver Code
 #x1 = -9; y1 = 3; x2 = 5; y2 = -7
 #center(x1, x2, y1, y2)
 a=[]
 b=[]
 for circle in circles:
  #for a in range(len(df['filename'])):
  #print(d['filename'][a])
  
  x, y, r = circle
  #print(circle)
  label=circle.ex['id']
  color=colors[circle.level]
  fig.add_shape(type="circle",
        xref="x", yref="y",
        x0=x-r, y0=y-r, x1=x+r, y1=y+r,
        # fillcolor="PaleTurquoise", # fill color if needed
        line_color=color,
        line_width=2,
    )
  x0=x-r; y0=y-r; x1=x+r; y1=y+r
  x,y=center(x0,x1,y0,y1)
  f.write(str(x)+","+str(y)+","+str(circle.ex['id'])+'\n')
# add child circles
# for child_circles in child_circle_groups:
#     for child_circle in child_circles:
#         x, y, r = child_circle
#         print("HELLO")
#         print(child_circle)
#         fig.add_shape(type="circle",
#             xref="x", yref="y",
#             x0=x-r, y0=y-r, x1=x+r, y1=y+r,
#             # fillcolor="PaleTurquoise", # fill color if needed
#             line_color="LightSeaGreen",
#             line_width=2,
#         )
    
# Set figure s
  




df = pd.read_csv("circles.csv")
fig.add_trace(go.Scatter(x=df['x'], y=df['y'], name='trace', 
           hovertext=df['label'],
           #base=0,
           opacity=0,
           #width=0.5
          ))
            
fig.update_layout(width=2000, height=2000, plot_bgcolor="white")
#fig4 = go.Figure(data=fig.data + fig1.data)   
fig.show()