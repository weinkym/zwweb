import requests
import threading
import time
from threading import Timer
import sys
import logging

g_access_token=''
g_update_time=time.localtime()
g_expires_in=7200
g_dx_expires_in=600

g_appid='wxddb81ec87b64db28'
#g_appsecret='bd2eb4735026bff4e8bbc974b26d3da7'
g_appsecret='114cd107e4a078a85c0d74ca032db10b'
g_url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'
g_headers={'Accept': 'application/json', 'Content-Type': 'application/json'}

g_lock=threading.Lock()

def get_access_token():
    logging.info('fun={},ident={}'.format(sys._getframe().f_code.co_name,threading.currentThread().ident))
    g_lock.acquire()
    temp=g_access_token
    # need_update=(len(temp) <= 0)
    # if need_update is False:
    #     validity_time=time.localtime(time.time()-g_expires_in+g_dx_expires_in)
    #     if g_update_time < validity_time:
    #         need_update = True
    g_lock.release()

    if len(temp) <= 0:
        update_access_token(True)
        g_lock.acquire()
        temp=g_access_token
        g_lock.release()
    else:
        validity_time=time.localtime(time.time()-g_expires_in+g_dx_expires_in)
        if g_update_time < validity_time:
            update_access_token(False)

    return temp

def update_access_token(sync=False):
    logging.info('fun={},ident={}'.format(sys._getframe().f_code.co_name,threading.currentThread().ident))
    logging.info('sync={}'.format(sync))
    if sync is True:
        request_access_token()
    else:
        sTimer = Timer(1, request_access_token)
        sTimer.start()

def request_access_token():
    logging.info(threading.currentThread())
    global g_access_token
    global g_expires_in
    global g_update_time

    r=requests.get(g_url.format(g_appid,g_appsecret),headers=g_headers)
    logging.info("request.status_code={},encoding={}".format(r.status_code,r.encoding))
    json_data=r.json()
    token=json_data['access_token']
    expires_in=json_data['expires_in']
    if type(token) is str and type(expires_in) is int:
        logging.info("update totken is sucess")
        g_lock.acquire()
        g_access_token=token
        g_expires_in=expires_in
        g_expires_in=605
        g_update_time=time.localtime()
        g_lock.release()
    else:
        logging.error("update totken is error")

    logging.info('expires_in={},g_access_token={}'.format(expires_in,g_access_token))


if __name__ == "__main__":
#     zwutil.init_log(True)
    update_access_token()
    
    # sTimer = Timer(1, get_access_token)
    # sTimer.start()
    # time.sleep(100)



