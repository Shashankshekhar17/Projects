import requests
from bs4 import BeautifulSoup
import os
import re
import shutil
import urllib.request
import time

downpath="Enter Download Path
name=input("Enter Movie Name: ")
os.chdir(downpath)
if(os.path.exists(name)):
    shutil.rmtree(name)
os.mkdir(name)
os.chdir(downpath + name + "\\")
quer=name.replace(" ", "+")
yearr=requests.get('https://www.imdb.com/find?q=' + quer +'&ref_=nv_sr_sm')
soup=BeautifulSoup(yearr.content, 'html.parser')
soup.prettify()
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
c=0
with open(name+ '-pages.txt', 'w+') as sta:
    with open(name+ '-list.txt', 'w+') as st:
        for i in soup.find_all('a'):
            data=i.get('href')
            if 'https:' in data:
                if '/files.html' in data:
                    if '/url?q' in data:
                        e=data.replace("/url?q=", "")
                        f=re.sub("&sa.*", "", e)
                        rtr=requests.get(f)
                        soup=BeautifulSoup(rtr.content, "html.parser")
                        for i in soup.find_all('div', class_='files-list'):
                            for q in i.find_all('a'):
                                a=q.get('href')
                                v="https://pagalworld.pw" + a
                                if '/p-' not in v:
                                    st.write(v)
                                    st.write('\n')
                                if '/p-' in v:
                                    c+=1
                                    if '/p-2' in v and c>2:
                                        print("", end="")
                                    else:
                                        sta.write(v)
                                        sta.write('\n')
st.close()
sta.close()

if (os.path.getsize(name + '-pages.txt')) > 100:
    fwe=open(name+ '-pages.txt', 'r')
    urrls=fwe.readlines() 
    with open(name +'-list.txt', 'a') as oofile:
        for urla in urrls:
            urlqq=urla.replace("\n", "")
            rqw=requests.get(urlqq)
            soup=BeautifulSoup(rqw.content, "html.parser")
            for iq in soup.find_all('div', class_='files-list'):
                for qw in iq.find_all('a'):
                    aq=qw.get('href')
                    va="https://pagalworld.pw" + aq
                    if '/p-' not in va:
                        oofile.write(va)
                        oofile.write('\n')
oofile.close()
fwe.close()

#script to get the download url(mp3 file)
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
    os.remove(name +'-pages.txt')
else:
    print('Not Found')
    os.remove(name +'-list.txt')
    os.remove(name +'-pages.txt')
    os.chdir(downpath)
if len(os.listdir(downpath+ name) ) == 0:
    os.rmdir(name)
file.close()