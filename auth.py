import requests

url='http://webhacking.kr/index.php?mode=auth_go'
payload={'answer':'9462a8c570c32302445a5ffb0ca3bf00'}
cookies={'PHPSESSID':'1gvdu8mjh0miihv90idtg3djj3'}
response=requests.post(url, data=payload, cookies=cookies)
print response.text
