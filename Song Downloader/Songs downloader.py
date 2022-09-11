import requests
from bs4 import BeautifulSoup
import os
import re
import shutil
import urllib.request
import time


name=input("Enter Movie Name: ")
os.chdir("C:\\Users\\Shashank\\Desktop\\")
if(os.path.exists(name)):
    shutil.rmtree(name)
os.mkdir(name)
os.chdir("C:\\Users\\Shashank\\Desktop\\"+ name + "\\")
quer=name.replace(" ", "+")
yearr=requests.get('https://www.imdb.com/find?q=' + quer +'&ref_=nv_sr_sm')
soup=BeautifulSoup(yearr.content, 'html.parser')
soup.prettify()
print("Movie Year Found: ", end="")
count=0
for i in soup.find_all('td', class_='result_text'):
    if(count == 0):
        y=i.text
        for s in y:
            if(count==0):
                dew=re.sub(".*\(", "", y)
                ert=re.sub("\)","", dew)
                tasd=re.sub("\s.*", "", ert)
                erte=re.sub("\D", "", tasd)
                count+=1
                print(erte)
print("\n")
lget=requests.get('https://www.google.com/search?q=' + name + " site:pagalworld.pw")
soup=BeautifulSoup(lget.content, 'html.parser')
soup.prettify()
cou=0
with open (name +'-list.txt','w+') as first:
    for i in soup.find_all('a'):
        data=i.get('href')
        if 'https:' in data:
            if '/files.html' in data:
                if '/url?q' in data:
                    if(cou == 0):
                        req=data.replace("/url?q=", "")
                        checkd=re.sub("&sa.*", "", req)
                        rtr=requests.get(checkd)
                        soup=BeautifulSoup(rtr.content, "html.parser")
                        for i in soup.find_all('div', class_='files-list'):
                            for q in i.find_all('a'):
                                a=q.get('href')
                                v="https://pagalworld.pw" + a
                                first.write(v)
                                first.write("\n")
                                cou+=1
                        
first.close()
#script to get the download url
if (os.path.getsize(name +'-list.txt')) > 150:
    print("Fetching Songs... ")
    if(os.path.exists(name +'.txt')):
        os.remove(name +'.txt')
    from bs4 import BeautifulSoup
    file=open(name + '-list.txt', 'r')
    urls=file.readlines() 
    with open(name +'.txt', 'x+') as ofile:
        for url in urls:
            urlq=url.replace("\n", "")
            r=requests.get(urlq)
            soup=BeautifulSoup(r.content, "html.parser")
            for i in soup.find_all('div', class_='downloaddiv'):
                for q in i.find_all('a'):
                    e=q.get('href').replace(" ", "%20")
                    ofile.write(e)
                    ofile.write("\n")
    ofile.close()
    file.close()
    print("Songs List Fetched")

#script to download the songs
    print("Downloading Songs ... Please Wait ")
    fil=open(name + ".txt", 'r+')
    te=fil.readlines()
    for urla in te:
        urlqa=urla.replace("\n", "")
        te=urlqa
        r=re.compile(".*/")
        d=re.sub(".*/" ,"" , te)
        e=re.sub("%20", " ", d)
        urllib.request.urlretrieve(urlqa,e)
    fil.close()
    print('All Songs Downloaded')
    os.remove(name + '.txt')
    os.remove(name +'-list.txt')
else:
    print('Not Found')
    os.remove(name +'-list.txt')
    os.chdir('C:\\Users\\Shashank\\Desktop\\')
if len(os.listdir('C:\\Users\\Shashank\\Desktop\\'+ name) ) == 0:
    os.rmdir(name)