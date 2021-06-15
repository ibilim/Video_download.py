##Video download 
import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl
import re
import json
import pprint
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode =ssl.CERT_NONE
url='https://www.youtube.com/watch?v=keo0dglCj7I'
videoId=re.findall(r'([ˆv=]\w+)',url)[0][1:]
print(videoId)
file=urllib.request.urlopen(url,context=ctx).read()

soup=BeautifulSoup(file,'html.parser')
tags=soup('script')
for tag in tags:
    if 'streamingData' in str(tag):
        content=tag.contents[0][30:-1]
        print(type(content),content)
        script=str(tag).split(',')
        script=script[1:-1]
        script=','.join(script)

import json
content_dict=json.loads(content)
formats=content_dict['streamingData']['formats']
#print(content_dict['streamingData']['formats'])
video_title=content_dict['videoDetails']['title']
all_formats=content_dict['streamingData']['adaptiveFormats']+formats
video_quality=['144p','240p','360p','480p','720p','1080p']
#print(content_dict['streamingData']['adaptiveFormats'])
head={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
for i in all_formats:
    if i['qualityLabel']=='480p':
        #req=urllib.request.Request(i.get('url'),headers=head)
        test=urllib.request.urlopen(i.get('url')).read()
        file_new=open('Click_link1.mp4','wb')
        file_new.write(test)
        file_new.close()
    else:
        print(':)))')
