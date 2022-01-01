import json
from os import popen
from re import template
import sys
import json
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from . import chart as c
import requests
import pprint
#sys.path.append('D:\study\csu33012-python-github\\')
from . import script2 as p
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
    out={}
    inp= request.POST.get('param')
    hello=run([sys.executable,'D:\study\csu33012-python-github\\cleardb.py'],shell=False,stdout=PIPE)
    kma=run([sys.executable,'D:\study\csu33012-python-github\\script2.py'],shell=False,stdout=PIPE)
    print(hello)
    print(kma)
    hel=run([sys.executable,'D:\\study\\GitHubVisualization\\test.py',inp],shell=False,stdout=PIPE)
    print(hel)
    #out=run([sys.executable,'D:\study\csu33012-python-github\\script2.py'],shell=False,stdout=PIPE)
    out = p.main()
    pprint.pprint(out)
    """json_pretty = json.dumps(out, sort_keys=True, indent=4)
    out=json_pretty"""
    print(out)
    for m in out:
        
        for k,v in m.items():
         
            
         print(str(k) +':'+str(v))
    CHART=run([sys.executable,'D:\\study\\GitHubVisualization\\buttonpython\\buttonpython\\chart.py',inp],shell=False,stdout=PIPE)
    #c.main()
    #js = json.dumps(out)
    print(CHART)
    
    return render(request,'index.html', {'data1': out})
    #return render(request,'index.html',{'data1':out})

def graph(request):
    return render(request,'file.html',{})
