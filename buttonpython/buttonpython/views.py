import json
import os
from os import popen
from queue import Empty
from re import template
import sys
import json
from buttonpython.settings import BASE_DIR

sys.path.append("..//")
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import render,redirect
from pymongo import message
print("This is the directory")
print(os.getcwd())

from script import chart as c
import requests
import pprint
import pandas as pd
#sys.path.append('D:\study\csu33012-python-github\\')
from script import script3 as p
from script import script2 as s
from script import script3 as scrip3
from script import script4 as scrip4
from script import chart   as a
from collections import defaultdict
from subprocess import Popen, PIPE, STDOUT
import sys
from subprocess import run,PIPE

from django.contrib import messages

#os.chdir("../")
sys.path.append(BASE_DIR)



def button(request):
    return render(request,'index.html')



# def output(request):
#     data=requests.get("https://www.google.com/")
#     print(data.text)
#     data=data.text
#     return render(request,'index.html',{'data':data})



def external(request):
    out={}
    file =open("data//userdata.txt") 
    df=file.read()
    cd=df.split(',')
    inp= str(cd[0])
    inp1=str(cd[1])

    # inp="esjmb"
    # inp1=str(84)
    print(str(inp))
    print(str(inp1))
    #print("hello"+str(inp1))
    hello=run([sys.executable,'script//cleardb.py'],shell=False,stdout=PIPE)
    kma=run([sys.executable,'script//script3.py'],shell=False,stdout=PIPE)
    print(hello)
    print(kma)
    #hel=run([sys.executable,'D:\\study//GitHubVisualization\\test.py',inp],shell=False,stdout=PIPE)
    #print(hel)
    hel=run([sys.executable,'script//churn.py',inp,inp1],shell=False,stdout=PIPE)
    kma=run([sys.executable,'script//script3.py'],shell=False,stdout=PIPE)
    print(hel)
    scripout=scrip3.main()
    if scripout=="error":
     return redirect("")
    #messages.error(request,"Sorry something went wrong ")  
    print(kma)
    #out=run([sys.executable,'D:\study\csu33012-python-github\\script2.py'],shell=False,stdout=PIPE)
    #out = p.main()
    #os.chdir("../")
    print(os.getcwd())
    #pprint.pprint(out)
    """json_pretty = json.dumps(out, sort_keys=True, indent=4)
    out=json_pretty"""
    #print(out)
    #################################################################printitng dictionary out in table form
    #for m in out:
        
     #   for k,v in m.items():   
            
            
      #   print(str(k) +':'+str(v))
    CHART=run([sys.executable,'script//chart.py'],shell=False,stdout=PIPE)
    #a.main()
#    c.main() ,inp, inp1
    #js = json.dumps(out)
    print(CHART.stdout)
    return render(request,'graph.html',{})
    #return render(request,'index.html', {'data1': out})
    #return render(request,'index.html',{'data1':out})

def graph(request):
    return render(request,'Churn_Rate.html','Churn_bar.html',{})
def home(request):
    return render(request,'index.html',{})    
def data(request):
    inp=""
    inp1=""
    with open("data//userdata.txt", "w+") as f:
      #f.write('username,date\n ')
      f.write(str(inp)+","+str(inp1)+"\n")
    hello=run([sys.executable,'script//cleardb.py'],shell=False,stdout=PIPE)
    inp= request.POST.get('param')
    inp1=request.POST.get('para')
    print(inp1)
    print(os.getcwd())
    with open("data//userdata.txt", "w+") as f:
      #f.write('username,date\n ')
      f.write(str(inp)+","+str(inp1)+"\n")
    hel=run([sys.executable,'script//test.py',inp],shell=False,stdout=PIPE)
    print(hel)
    out=run([sys.executable,'script//script2.py'],shell=False,stdout=PIPE)
    print(out)
    #json_pretty = json.dumps(out, sort_keys=True, indent=4)
    out=s.main()
    #out=json_pretty
    print(out)
    a=[]
    if out == "error":
      return redirect ("")
    #messages.error(request, 'Not Found')
    for m in out:
       a=[]    
    try:
         for k,v in m.items():   
          if k == 'repo':
            for i in m.get('repo'):
                print(i)
                a.append(i)
                     
         else:   
          print(str(k) +':'+str(v))
    except Exception as e:
     return redirect("")
     #messages.error(request, 'User Not Found')
    #   if not a:
    #      a.append(emp)
    #      print("error")
    #      out=emp
    # print(a)
    # print("out")
    # print(out)      
    return render(request,'table.html', {'data1': out,'repos':a})



def compare(request):
    out={}
    file =open("data//userdata.txt") 
    df=file.read()
    cd=df.split(',')
    inp= str(cd[0])
    inp1=str(cd[1])

    # inp="esjmb"
    # inp1=str(84)
    print(str(inp))
    print(str(inp1))
    #print("hello"+str(inp1))
    hello=run([sys.executable,'script//cleardb.py'],shell=False,stdout=PIPE)
    kma=run([sys.executable,'script//script4.py'],shell=False,stdout=PIPE)
    print(hello)
    print(kma)
    
    
    #hel=run([sys.executable,'D:\\study//GitHubVisualization\\test.py',inp],shell=False,stdout=PIPE)
    #print(hel)
    hel=run([sys.executable,'script//filesize.py',inp,inp1],shell=False,stdout=PIPE)
    kma=run([sys.executable,'script//script4.py'],shell=False,stdout=PIPE)
    print(hel)
    print(kma)
    scripout= scrip4.main()
    if scripout=="error":
     return redirect("")
    #messages.error(request,"Sorry something went wrong ") 
    CHART=run([sys.executable,'script//chart1.py'],shell=False,stdout=PIPE)
    print(CHART.stdout)
    print("current location")
    print(os.getcwd()) 
    return render(request,'compare.html',{})   

def about(request):
    return render(request,'about.html',{})      