from selenium import webdriver  
import time  
import re
import requests
import os
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
os.chdir("Download Path")

nam=input("Enter Song Name: ")
name=nam.replace(" ", "+")
print("Searching...")
r=requests.get('https://www.google.com/search?q='+name+'&rlz=1C1UEAD_enIN958IN958&source=lnms&tbm=vid&sa=X&ved=2ahUKEwisqNXigoP7AhWcy6ACHUx7DeEQ_AUoAXoECAIQAw&biw=1536&bih=722&dpr=1.25')
soup=BeautifulSoup(r.content,'html.parser')
c=0
for rt in soup.find_all('a'):
    qw=rt.get('href')
    if 'youtube' in qw:
        if(c<1):
            e=qw.replace("/url?q=", "")
            rg=re.sub(r'&sa.*',"",e)
            son=re.sub(r'www.youtube','ssyoutube',rg)
            so=re.sub(r'%3F',"?",son)
            song=re.sub(r'%3D',"=",so)
            c+=1
options=Options()
options.headless=True
s=Service("ChromeDriverPath")
driver = webdriver.Chrome(service=s,options=options) 
driver.get(song)
time.sleep(7)
w=driver.page_source
t=BeautifulSoup(w,features="lxml")
if 'converter' in w:
    for i in t.find_all('div', class_="def-btn-box"):
        for q in i.find_all('a'):
            link=q.get('href')
    print("Downloading....Please Wait")
    urllib.request.urlretrieve(link,nam.title()+'.mp4')
    print("Completed")
else:
    print("Sorry this song cannot be downloaded")