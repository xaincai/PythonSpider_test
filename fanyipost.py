#!/usr/bin/python
#  coding: utf-8
import urllib2
import urllib
import json
import time
import random
import hashlib

# url = "http://fanyi.youdao.com/translate_o?"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
"Accept":" application/json, text/javascript, */*; q=0.01",
"X-Requested-With":" XMLHttpRequest",
"User-Agent":" Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Accept-Language":" zh-CN,zh;q=0.9"

}

key = raw_input("translation for:  ")

u = 'fanyideskweb'
d = key
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'ebSeFb%=XZ%T[KZ)c(sy!'

md5 = hashlib.md5()
md5.update(u)
md5.update(d)
md5.update(f)
md5.update(c)
sign = md5.hexdigest()
data = {
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":f,
"sign":sign,
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}
data = urllib.urlencode(data)
request = urllib2.Request(url,data=data,headers=headers)
respose = urllib2.urlopen(request)
line = json.load(respose)
print line['translateResult'][0][0]['tgt']
# print respose.read()