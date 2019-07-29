from django.test import TestCase

import xml
from xml.dom.minidom import Document
import time

MESSAGE_TYPE_TEXT='text'
MESSAGE_TYPE_IMAGE='image'

class Message:
    ToUserName=''
    FromUserName=''
    CreateTime=''
    MsgType=''
    PicUrl=''
    MediaId=''
    MsgId=''
    Content=''
    def __str__(self):
        str_CreateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(self.CreateTime)))
        if self.MsgType == MESSAGE_TYPE_TEXT:
            return '{} type={} content={}'.format(str_CreateTime,self.MsgType,self.Content)

        if self.MsgType == MESSAGE_TYPE_IMAGE:
            return '{} type={} PicUrl={}'.format(str_CreateTime,self.MsgType,self.PicUrl)
        return "unkown type"

def getMessageItemContent(dom,name):
    itemlist = dom.getElementsByTagName(name)
    if len(itemlist) == 1:
        item=itemlist[0]
        node=item.firstChild
        if hasattr(node,'data'):
            return node.data
        return node


def appendItemCDATASection(doc,item_root,key,value):
    item=doc.createElement(key)
    node=doc.createCDATASection(value)
    item.appendChild(node)
    item_root.appendChild(item)


def appendItem(doc,item_root,key,value):
    item=doc.createElement(key)
    node=doc.createTextNode(value)
    item.appendChild(node)
    item_root.appendChild(item)

def createResponseMessage(ToUserName,FromUserName,text):
    doc=Document()
    item_xml=doc.createElement('xml')

    appendItemCDATASection(doc,item_xml,'ToUserName',ToUserName)
    appendItemCDATASection(doc,item_xml,'FromUserName',FromUserName)
    appendItemCDATASection(doc,item_xml,'Content',text)

    timestamp=time.mktime(time.localtime())
    timestamp=str(int(timestamp))
    appendItem(doc,item_xml,'CreateTime',timestamp)

    doc.appendChild(item_xml)
    res=doc.toprettyxml(indent='')
    # res=doc.toxml()
    delete_str='<?xml version="1.0" ?>'
    if res.startswith(delete_str):
        res=res[len(delete_str):-1]

    res=res.encode(encoding='utf-8')
    return res


# dom = xml.dom.minidom.parse('/Users/miaozw/Documents/message.xml')
# msg = Message()

# msg.ToUserName=getMessageItemContent(dom,'ToUserName')
# msg.FromUserName=getMessageItemContent(dom,'FromUserName')
# msg.CreateTime=getMessageItemContent(dom,'CreateTime')
# msg.MsgType=getMessageItemContent(dom,'MsgType')
# msg.PicUrl=getMessageItemContent(dom,'PicUrl')
# msg.MediaId=getMessageItemContent(dom,'MediaId')
# msg.MsgId=getMessageItemContent(dom,'MsgId')
# msg.Content=getMessageItemContent(dom,'Content')


# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))
# user = User()
# Create your tests here.
# timestamp=time.mktime(time.localtime())
# timestamp=str(int(timestamp))
# print(type(timestamp))
# print(timestamp)
res=createResponseMessage("a","b","this message is ok")

print(res)
