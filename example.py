from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from sys import argv
import socket
import time
import re

# timeout
socket.setdefaulttimeout(6)

#locate your phantomjs
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')

def getCover(index, minScore):
    driver.get("http://h.bilibili.com/dy" + str(index))
    time.sleep(3)

    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "html.parser")

    scoreObj = bsObj.find("div", {"title": "评分"})
    if(False == hasScore(scoreObj)):
        print("no score, return")
        return
    score = getScore(scoreObj)

    if(score < minScore):
        print("score is less than minScore, return." + str(score) + ":" + str(minScore))
        return

    imgObj = bsObj.find("img", {"style":"opacity: 1;"})
    if(False == hasImg(imgObj)):
        print("no img, return")
        return

    address = getImgAddress(imgObj)
    print(address)
    try:
        urlretrieve (address, str(index)+'.jpg')
    except Exception as e:
        print(e)

def hasScore(scoreObj):
    if scoreObj is None:
        return False
    if scoreObj.div is None:
        return False
    if scoreObj.div.string is None:
        return False
    return True

def getScore(scoreObj):
    return (int)(scoreObj.div.string);

def hasImg(imgObj):
    if imgObj is None:
        return False
    if imgObj.attrs is None:
        return False
    if imgObj.attrs["src"] is None:
        return False
    return True

def getImgAddress(imgObj):
    return imgObj.attrs["src"]

def getAll(beginIndex, endIndex, minScore):
    for i in range(beginIndex,endIndex):
        try:
            getCover(i, minScore)
        except Exception as e:
            print(e)

first = (int)(argv[1])
last = (int)(argv[2])
minScore = (int)(argv[3])

getAll(first,last,minScore)
