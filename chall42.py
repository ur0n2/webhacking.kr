import requests

url='http://webhacking.kr/challenge/web/web-20/index.php?down=dGVzdC56aXA='
cookies={'PHPSESSID':'89oojt3s1bilc5o2528i651hv4'}

response=requests.post(url, cookies=cookies)
print response.text