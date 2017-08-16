
import  sys,os,hashlib


if __name__ == '__main__':




    hash=hashlib.md5()
    hash.update("hello".encode())
    print(hash.hexdigest())
