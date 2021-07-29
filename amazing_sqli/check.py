# -*- coding:utf8 -*-
import sys
import re
import requests
import time
import random
from urllib.request import urlopen

s=requests.Session()

User_Agent='Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'

#除了返回的正常/错误，其余不输出任何信息，且需要设置超时时间！

# 检查网页能否正常打开
def check1(url):

    try:
        # response=requests.get(url,headers={'User-Agent':random.choice(User_Agent)}) 
        # code=response['Status code']
        resp = urlopen(url,timeout=2)
        code = resp.getcode()
        if code == 200 :
            print("Check1 success, 登录网页可以正常打开")
    except Exception as e:
        print("Check1 error, 登录网页无法正常打开")
        return False
    return True

def check2(url):

    try:
        # response=requests.get(url,headers={'User-Agent':random.choice(User_Agent)}) 
        # code=response['Status code']
        resp = urlopen(url,timeout=2)
        code = resp.getcode()
        if code == 200 :
            print("Check2 success, 留言板展示网页可以正常打开")
    except Exception as e:
        print("Check2 error, 留言板展示网页无法正常打开")
        return False
    return True

def check3(url):

    try:
        # response=requests.get(url,headers={'User-Agent':random.choice(User_Agent)}) 
        # code=response['Status code']
        resp = urlopen(url,timeout=2)
        code = resp.getcode()
        if code == 200 :
            print("Check3 success, 发布留言网页可以正常打开")
    except Exception as e:
        print("Check3 error, 发布留言网页无法正常打开")
        return False
    return True

# 判断网页sql注入是否成功
def check4(url):
    try:
        error = s.post(url + r"/?inject=1'",timeout=2)
        error = error.text
        result = re.search("error",error)
        if result:
            print("Check4 success, 网页存在sql注入")
    except Exception as e:
        print("Check4 error, sql未成功注入")
    return True


def checker(host, port):
    try:
        url = "http://"+ip+":"+str(port)
        url1 = url + "/board.html"
        url2 = url + "/share.php"
        if check1(url) and check2(url1) and check3(url2) and check4(url) :
            return (True,"IP: "+host+" OK","Port: "+str(port)+" OK")
    except Exception as e:
        return (False,"IP: "+host+" is down, "+str(e))

if __name__ == '__main__':
    # ip=sys.argv[1]
    ip="127.0.0.1"
    # port=int(sys.argv[2])
    port="8302"
    print(checker(ip,port))

