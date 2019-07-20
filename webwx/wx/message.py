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

def parseString(string):
    dom = xml.dom.minidom.parseString(string)
    msg = Message()
    msg.ToUserName=getMessageItemContent(dom,'ToUserName')
    msg.FromUserName=getMessageItemContent(dom,'FromUserName')
    msg.CreateTime=getMessageItemContent(dom,'CreateTime')
    msg.MsgType=getMessageItemContent(dom,'MsgType')
    msg.PicUrl=getMessageItemContent(dom,'PicUrl')
    msg.MediaId=getMessageItemContent(dom,'MediaId')
    msg.MsgId=getMessageItemContent(dom,'MsgId')
    msg.Content=getMessageItemContent(dom,'Content')
    return msg

def sendMessage(ToUserName,FromUserName,text):
    pass