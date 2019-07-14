from django.shortcuts import render

from django.http import HttpResponse
import hashlib

def index(request):
    msg='scheme={},path={},method={},encoding={},session={},META={}'.format(request.scheme,request.path,request.method,
    request.encoding,request.session,request.META)
    print('msg={}'.format(msg))
    token='wx2019mzw'
    # if request.method == request.GET:
    signature = request.GET.get("signature")
    echostr = request.GET.get("echostr")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    hashcode = sha1.hexdigest()
    print("token={},signature={},echostr={},timestamp={},nonce={}".format(token,signature,echostr,timestamp,nonce))
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("Hello, world. You're at the polls index.msg={}".format(msg))

    
# Create your views here.
