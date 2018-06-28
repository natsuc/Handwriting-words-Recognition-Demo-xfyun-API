#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import time
import urllib
import json
import hashlib
import base64



def main():
    f = open("003.jpg", 'rb')
    file_content = f.read()
    base64_image = base64.b64encode(file_content)
    body = urllib.urlencode({'image': base64_image})

    url = 'http://webapi.xfyun.cn/v1/service/v1/ocr/handwriting'
    api_key = 'XXX' #APIKEY
    param = {"language": "en", "location": "true"}

    x_appid = 'XXX' #APPID
    x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib2.Request(url, body, x_header)
    result = urllib2.urlopen(req)
    #json.load(result)
    result = result.read()
    #print result #str


    rdata=json.loads(result) #转换成字典
    #print type(rdata) #dict

    #print len(rdata['data']["block"][0]['line']) #list长度
    file = open("Document.txt", "a")





        #解析json结构后,轮询
    for i in range(0,len(rdata['data']["block"][0]['line'])):

        temp = rdata['data']["block"][0]['line'][i]['word'][0]['content']
        temp=temp.encode("utf-8")
        file.write(temp+"\n")
        print temp
        #print rdata['data']["block"][0]['line'][i]['word'][0]['content']

    file.close()
    #print rdata['data']["block"][0]['line'][0]['word'][0]['content'] #打印一次


    return


if __name__ == '__main__':
    main()