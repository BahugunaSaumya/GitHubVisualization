from os import popen
from django.shortcuts import render
import requests
from collections import defaultdict
from subprocess import Popen, PIPE, STDOUT
import sys
from subprocess import run,PIPE
def button(request):
    return render(request,'index.html')
def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'index.html',{'data':data})
def external(request):
    
    inp= request.POST.get('param')
    hello=run([sys.executable,'D:\study\csu33012-python-github\\cleardb.py'],shell=False,stdout=PIPE)
    print(hello)
    hel=run([sys.executable,'D:\\study\\GitHubVisualization\\test.py',inp],shell=False,stdout=PIPE)
    print(hel)
    out=run([sys.executable,'D:\study\csu33012-python-github\\script2.py'],shell=False,stdout=PIPE)
    print(out)
    
   
    return render(request,'index.html',{'data1':out.stdout})