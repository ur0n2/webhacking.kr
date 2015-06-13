import httplib
import requests

url="http://webhacking.kr/challenge/codeing/code5.html?hit=ur0n2"
cookie=dict(PHPSESSID="nu9fgj5udjf1d8ln6t3dqj5n46")#,expires="Thu, 01 Jan 1970 00:00:01 GMT")
for i in xrange(100):
  r=requests.get(url,cookies=cookie)
  print i

