import requests
import re
def get():
     html=requests.get('http://finance.ifeng.com/app/hq/stock/sh000001/')
     html.encoding='utf-8'
     d=re.findall(r'''/>(.*)%</font>''',html.text)#获取股指数字
     dt=re.findall(r'''target='_blank'>(.*)</a>''',html.text)#获取股指名称
     for i in range(3):     
            print(dt[i+1],d[i],'%')