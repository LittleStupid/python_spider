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

def getCover(index):
    driver.get("http://h.bilibili.com/dy" + str(index))
    time.sleep(3)

    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "html.parser")
    img = bsObj.find("img", {"style":"opacity: 1;"})

    if img is None:
        return
    if img.attrs is None:
        return
    if img.attrs["src"] is None:
        return

    try:
        urlretrieve (img.attrs["src"], str(index)+'.jpg')
    except Exception as e:
        print(e)

def getAll(beginIndex, endIndex):
    for i in range(beginIndex,endIndex):
        try:
            getCover(i)
        except Exception as e:
            print(e)

first = (int)(argv[1])
last = (int)(argv[2])

getAll(first,last)
