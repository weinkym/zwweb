from django.test import TestCase
import hashlib
import logging
import time
import requests
# import webwx.zwutil as zwutil
# Create your tests here.

def test3():
    u'''get带参数、带headers测试'''
    url='http://47.110.48.0:80/wx/'
    params = {'show_env': '8'}
    headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*','User-Agent': 'python-requests/2.18.3','token':'avc0901123'}
    # r = requests.get('http://47.110.48.0:80/wx/', params=params,headers=headers)

    r = requests.post(url, data={'key1':'value1','key2':'value2',},
    headers={'Content-Type':'multipart/form-data'},cookies={"username":"bobobk"})
    print('r={},content={}'.format(type(r),r.content))
    # r._content
    # r3 = r.json()
    # print(r3)
    # connect = r3.get('headers').get('Connection')
    # print('connect={}'.format(connect))

# test3()

temp=time.strftime("%Y%m%d%H%M%S", time.localtime())
print(temp)