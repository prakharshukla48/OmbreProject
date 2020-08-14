import requests 
import csv
from bs4 import BeautifulSoup
import time
import re 
lists = []
lists2 = []
url = "https://www.bandsintown.com/e/1020662209-ellie-goulding-at-live-stream?came_from=257&utm_medium=web&utm_source=home&utm_campaign=event"
page = ''
while page == '':
    try:
        page = requests.get(url)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue    
soup = BeautifulSoup(page.content,"html.parser")
#title of the event
title = soup.title.string
lists.append(title)
urlartist = "https://www.bandsintown.com/a/271336-ellie-goulding?came_from=257&utm_medium=web&utm_source=artist_event_streaming_page&utm_campaign=artist"
rart = ''
while rart == '':
    try:
        rart = requests.get(urlartist)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue
soupr = BeautifulSoup(rart.content,'html.parser')
#artist name of the event
artname = soupr.find('div',attrs = {'class':'_2tYMEzR8cMuGARygsRnsC_'})
artname = artname.h1.string
lists.append(artname)
#start time of the event(maybe encrypted in javascript)
start_time = soup.find_all('div',attrs = {'class':'_3kXAsJ0DPskjq42LFJzTpg'},limit =1)
lists.appebnd(start_time)

# genres of the artist 
genres = soupr.find('div',attrs={'class':'_2jwlhF_qo6XQLXdKdqXzMx'})
genres = genres.string
lists.append(genres)
# facebook page of the artist 
anchor = soupr.find_all('a')
for link in anchor: 
    if link.get('href') == "https://www.facebook.com/elliegoulding/":
        lists.append(link.get('href')) 
        break
# Event poster 
poster = soup.find_all('a',attrs = {'class':'_3FxoLllHIYDsTLMcW1mAl8'},limit = 1)
for link in poster:
    lists.append(link.get('href'))    
#link of live stream  
stream = soupr.find_all('a',attrs = {'class':'_6PQxOPPUFGit_6KHJb0bW'},limit = 1)    
for link in stream:
    lists.append(link.get('href'))
#stream link
ellie = soup.find_all("a",text = re.compile('ellie'),limit=1)
for link in ellie:
    lists.append(link.get('href'))
#link of the page of all popular livestream 
#we will need to create a new request here
url3 = "https://www.bandsintown.com/?came_from=257&hide_homepage=true&sort_by_filter=Number+of+RSVPs"    
rss = ''
while rss == '':
    try:
        rss = requests.get(url3)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue
souped = BeautifulSoup(rss.content,'html.parser')
popular = souped.find_all('a',attrs = {'class':'_3UX9sLQPbNUbfbaigy35li'}) 
for links in popular:
    lists.append(links.get('href'))
with open ('main.csv','w') as file:
   writer=csv.writer(file)
   for row in lists:
      writer.writerow(row)
   for row2 in lists2:
       writer.writerow(row2)

