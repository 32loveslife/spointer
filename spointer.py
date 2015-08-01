#encoding='utf-8'
'''2015-08-01
   Github.com/hhyy0302
   Modules that need:     Requests   
'''
'User interface'
import index
import getstock 
print();print('0: [exit] for exit');print('1: [index] for index');print('2: [StockCode] for stock: 601111');print();
def start():
    try:
          command =input('Your Command is: ')    
    except IOError: print('IOError')
    else:
         if command=="index":
            index.get()
            start()        
         if command=='exit':
                exit;
         else:getstock.get(command);start()
start()


