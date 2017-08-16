import  time
import  datetime


def log():

    with open('log','a+',encoding='utf-8') as log:
         log.writelines(time.strftime("%Y年%m月%d日",time.localtime()))



class mynew(object):
    def __init__(self):
        print("__init__method")
    def __new__(cls, *args, **kwargs):
        print("new_method")
    def __del__(self):
        print("destroy method")


class mysetitem(object):
    def __setitem__(self, key, value):
        print('key(%d)value(%d)',key,value)
    def __getitem__(self, item):
        if item=='jackwu':
            print('jackwu is%d')



class cmp(object):
    def __init__(self,x):
        self.data=x
    def __cmp__(self, other):
        if other.data==self.data:
            print('xxxx')

if __name__ == '__main__':

     c=cmp(2)
     x=cmp(2)
     if c==x:
         print('ok ===')


