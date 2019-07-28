from django.shortcuts import render

from django.http import HttpResponse
import hashlib
import logging
import time
import webwx.zwutil as zwutil
import webwx.settings as settings
from . import wxtoken
from . import message as MSG
import webwx.ocr_baidu as OCR

def test(request,index):
    return HttpResponse("test method={},index={}".format(request.method,index))

g_is_first=True
if g_is_first is True:
    g_is_first = False
    zwutil.init_log()
    wxtoken.update_access_token(False)


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
        # return HttpResponse("post postBody={}".format(postBody))
        msg=MSG.parseString(postBody)
        logging.info("msg={}".format(msg))
        
        if msg.Content == 'TEST':
            res=MSG.createResponseMessage(msg.FromUserName,msg.ToUserName,'this message is ok')
            # logging.info("respose msg={}".format(res))
            # res=res.encode(encoding='utf-8')
            logging.info("respose msg={} \ntype={}".format(res,type(res)))
            return HttpResponse(res)
        if msg.MsgType == MSG.MESSAGE_TYPE_IMAGE:
            logging.info('msg.PicUrl={}'.format(msg.PicUrl))
            ocr_res=OCR.get_image_ocr_url(msg.PicUrl)
            logging.info('ocr_res={}'.format(ocr_res))
            ocr_str=''.join('{}\n'.format(str(i)) for i in ocr_res)
            res=MSG.createResponseMessage(msg.FromUserName,msg.ToUserName,ocr_str)
            return HttpResponse(res)

        return HttpResponse("success")
    # logging.info("content={}".format(request.content))
    return HttpResponse("mzw={}===time".format(request.method))

# Create your views here.
