from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import time
from sys import argv
import socket

socket.setdefaulttimeout(10)

headers = set()

def getHeader(index):
    html = urlopen("http://h.bilibili.com/dy" + str(index))
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except http.client.IncompleteRead:
        return

    if( bsObj ):
        image = bsObj.find("img", {"class": "person_head"})
        if(image):
            if("src" in image.attrs):
                time.sleep(1)
                address = image.attrs["src"]
                if address in headers:
                    return

                headers.add(address)
                print(address)

                try:
                    urlretrieve (image.attrs["src"], str(index)+'.jpg')
                except FileNotFoundError:
                    print("file is not found")
                except ValueError:
                    print("Value error")
                except Exception:
                    print("Other error")

def getAll(beginIndex, endIndex):
    for i in range(beginIndex,endIndex):
        try:
            getHeader(i)
        except Exception as e:
            print(e)

first = (int)(argv[1])
last = (int)(argv[2])

getAll(first,last)
