


import requests


#登陆ace测试平台
def login():
    url = 'https://ace-test.altstory.com/passport/login'
    data = {
        'username': 'test',
        'password': 'test',
        'remember': 'false'
    }

    r = requests.post(url=url, data=data)
    # cookies = r.cookies
    # print(r.json())
    uid,token = r.json()['data']['uid'],r.json()['data']['token']
    headers = {
        'uid': str(uid),
        'token': token,
        'Content-Type': 'application/json'
    }
    return headers
