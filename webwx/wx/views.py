from django.shortcuts import render

from django.http import HttpResponse
import hashlib
import logging
import time
import webwx.zwutil as zwutil
import webwx.settings as settings

def test(request,index):
    return HttpResponse("test method={},index={}".format(request.method,index))

g_is_first=True
if g_is_first is True:
    g_is_first = False
    settings.TIME_ZONE='Asia/Shanghai'
    settings.USE_TZ=False
    zwutil.init_log()

def is_wx_message(request):
    if request.method == 'GET':
        token='wx2019mzw'
        signature=request.GET.get("signature")
        echostr=request.GET.get("echostr")
        timestamp=request.GET.get("timestamp")
        nonce=request.GET.get("nonce")
        check_key_list = [signature,echostr,timestamp,nonce]
        if zwutil.check_str_list(check_key_list):
            key_list = [token, timestamp, nonce]
            key_list.sort()
            text=''
            for obj in key_list:
                text=text+obj
            sha1 = hashlib.sha1()
            sha1.update(text.encode('utf-8'))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr

    return False


def index(request):
    logging.warn("test===={}".format(time.strftime("%Y%m%d%H%M%S", time.localtime())))
    msg='scheme={},path={},method={},encoding={},session={},META={}'.format(request.scheme,
    request.path,request.method,
    request.encoding,request.session,request.META)
    logging.warn(msg)
    if request.method == 'GET':
        logging.info("the GET method")
        username=request.GET.get("username")
        is_wx=is_wx_message(request)
        if is_wx is not False:
            return HttpResponse(is_wx)

        return HttpResponse("GET username={}".format(username))
    if request.method == 'POST':
        logging.info("the POST method")
        concat = request.POST
        postBody = request.body
        logging.info('concat={}'.format(concat))
        logging.info(type(postBody))
        logging.info('postBody={}'.format(postBody))
        return HttpResponse("post postBody={}".format(postBody))
    # logging.info("content={}".format(request.content))
    return HttpResponse("mzw={}===time".format(request.method))
   # print('msg={}'.format(msg))
    # token='wx2019mzw'
    # if request.method == request.GET:
    # signature = request.GET.get("signature")
    # echostr = request.GET.get("echostr")
    # timestamp = request.GET.get("timestamp")
    # nonce = request.GET.get("nonce")
    # list_t = [token, timestamp, nonce]
    # list_t.sort()
    # sha1 = hashlib.sha1()
    # map(sha1.update, list_t)
    # hashcode = sha1.hexdigest()
    # print("token={},signature={},echostr={},timestamp={},nonce={},hashcode={}".format(token,signature,
    # echostr,timestamp,nonce,hashcode))
    # return HttpResponse(msg)
    # if hashcode == signature:
    #     print("ok==")
    #     return HttpResponse(echostr)
    # else:
    #     print("!!!!==")
    #     return HttpResponse(echostr)
        # return HttpResponse("Hello, world. You're at the polls index.msg={}".format(msg))

    
# Create your views here.
