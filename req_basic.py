import requests

url='http://ipip.kr'

param={'kk':'17d41ef680b34a006abbe1a9ee6d54b5'}
#files={'upfile': ('tmp-1427959188',open('tmp-1427959188','rb'))}
cookies={'PHPSESSID':'brieopfbm174l5pldrp06it4c5'}
#response=requests.get(url,cookies=cookies)
response=requests.post(url,data=param,cookies=cookies)

print response.text
