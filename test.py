#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#https://stackoverflow.com/questions/19735250/running-a-python-script-from-php
import sys
import datetime
import json
import requests
import sys
from time import sleep,gmtime, strftime,localtime


def post_dingding(self,filename_):
    payload_simple = '{"msgtype": "link", "link": { "text":"'+ sales_list["text"] +'", "title":"'+ filename_ +' ' +sales_list["title"] +'","picUrl":"'+sales_list["picUrl"] +'", "messageUrl":"' + sales_list["messageUrl"]+filename_+ '"   } }'
    print payload_simple

    #    #if save_to_file: fid.write(payload_simple+next_line)
    #    if save_to_file: fid.write(payload_simple+'\n')
    headers = {'content-type': 'application/json;charset=utf-8', 'Accept-Charset': 'UTF-8'}
    #    if sw_exclusion==False:
    quote_page = ['https://oapi.dingtalk.com/robot/send?access_token=f982a746638fdf2a85bdcc8f3200398136ff38bf2c650d013e70cff583e74cb8','https://oapi.dingtalk.com/robot/send?access_token=ad42b9342637340b04fc950df42c30fe20ec5738d1071af15fae401c7c47c749']
    for url in quote_page:
        r=requests.post(url, data=payload_simple, headers=headers)
        print r
        sleep(0.2)

with open('sending_list.json', 'r') as f:
        sales_list = json.load(f)

post_dingding(sales_list,sys.argv[1])
print sys.argv[1]
#print 'this is from python\n'
#print(sys.argv[0])
#print sales_list
