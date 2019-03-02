import requests
res=requests.get("https://www.ptt.cc/bbs/Tech_Job/index.html")
#print(res.text)
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text,'html.parser')
tag_name="div.title a"
articles=soup.select(tag_name)
#print(articles)
for art in articles:
    #print(art)
    print(art['href'],art.text)
