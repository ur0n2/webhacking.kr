import requests
url='http://webhacking.kr/challenge/web/web-37'
#cookies={'PHPSESSID':'aaaaaaaaaaaaaaaaaaaaaaaaaa'}
cookies={'PHPSESSID':'bbbbbbbbbbbbbbbbbbbbbbbbbb'}

for i in xrange(100):
    print requests.get(url, cookies=cookies).text
