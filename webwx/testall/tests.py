from django.test import TestCase

import requests
# Create your tests here.

def test3():
    u'''get带参数、带headers测试'''
    params = {'show_env': '8'}
    headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*','User-Agent': 'python-requests/2.18.3','token':'avc0901123'}
    r = requests.get('http://127.0.0.1:8000/wx/', params=params,headers=headers)
    print('r={},content={}'.format(type(r),r.content))
    # r._content
    # r3 = r.json()
    # print(r3)
    # connect = r3.get('headers').get('Connection')
    # print('connect={}'.format(connect))

test3()