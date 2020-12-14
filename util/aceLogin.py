


import requests


#登陆ace测试平台
def login():
    url = ''
    data = {

    }

    r = requests.post(url=url, data=data)
    # cookies = r.cookies
    # print(r.json())
    uid,token = r.json()['data']['uid'],r.json()['data']['token']
    headers = {

    }
    return headers
