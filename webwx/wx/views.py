from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    msg='scheme={},path={},method={},encoding={},session={},META={}'.format(request.scheme,request.path,request.method,
    request.encoding,request.session,request.META,)
    print(msg)
    return HttpResponse("Hello, world. You're at the polls index.msg={}".format(msg))
# Create your views here.
