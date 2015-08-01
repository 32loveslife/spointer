'''Introduction
sname: Stock Name
cprice: Current Price
yprice:Yesteday's Price
chrate:Change rate
 '''
import requests
import re
def get(number):
        if len(number)<7: number='0'+str(number);
        url='http://quotes.money.163.com/'+number+'.html';
        html=requests.get(url);html.encoding='utf-8';
        check=re.findall(r'''http://img1.cache.netease.com/2009/(.*)/error_tips.gif''',html.text);check=str(check);check=check[2:-2];
        if check!='error':
             sname=re.findall(r'''name: '(.*)',''',html.text);sname=str(sname);sname=sname[2:-2];  cprice=re.findall(r'''price: '(.*)',''',html.text);cprice=str(cprice);cprice=cprice[2:-2];yprice=re.findall(r'''yesteday: '(.*)',''',html.text); yprice=str(yprice);yprice=yprice[2:-2];
             chrate=float(cprice)-float(yprice); print(sname,'--',cprice,'RMB ',yprice,'RMB ',round(chrate,2),'%');
        else:print('StockCodeError!---Example:601111')
        #print(check)