from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from sys import argv
import socket
import time
import re

# timeout
# socket.setdefaulttimeout(10)

#locate your phantomjs
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')

def getCover(index)
    driver.get("http://h.bilibili.com/dy" + str(index))
    time.sleep(3)

    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "html.parser")
    img = bsObj.find("img", {"style":"opacity: 1;"})

    try:
        urlretrieve (image.attrs["src"], str(index)+'.jpg')
    except FileNotFoundError:
        print("file is not found")
    except ValueError:
        print("Value error")
    except Exception:
        print("Other error")

# driver.get("http://h.bilibili.com/dy6570")
# time.sleep(3)
# pageSource = driver.page_source

# bsObj = BeautifulSoup(pageSource, "html.parser")

# img = bsObj.find("img", {"style":"opacity: 1;"})
# score = bsObj.find("div", {"title":"评分"})
# names = bsObj.find("p", {"class":"name"})

# print(img)
# print("###")

# print(score)
print("###")

# print(names)
# driver.close()
# time.sleep(5)


# def getCover(index)
#
# def getAll(beginIndex, endIndex)
#     for i in range(beginIndex,endIndex):
#         try:
#             getCover(i)
#         except Exception as e:
#             print(e)
