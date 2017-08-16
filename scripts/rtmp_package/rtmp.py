
#jackwu

import  sys
import  os
import  threading
import  queue
import  io
import  struct
import  math,socket

SIG_SIZE=0X3
HEADER_VERSION=0X1
HEADER_HAS=0X1
HEADER_SIZE=0X4




flv_queue=queue.Queue()


#元数据解析
def  metedata_handler_rtmp():
    pass

#音频封装
def  audio_handler_rtmp():
     pass


def   video_handler_rtmp():
      pass


class flv_header(object):
    def __init__(self,sig,version,has,size):
        self.sig=sig
        self.version=version
        self.has=has
        array=bytearray(has)

        self.has_aud=(array[0]>>2)&0x1
        self.has_vid=(array[0]&0x1)
        self.size=size
        pass
    def  getsig(self):
        return self.sig
    def getversion(self):
        return self.version
    def gethas_aud(self):
        return self.has_aud
    def gethas_vid(self):
        return self.has_vid
    def gethas(self):
        return self.has
    def __str__(self):
        return "header info :"+str(self.sig)+str(self.version)+\
               str(self.has_vid)+str(self.has_aud)+str(self.size)


class metedata(object):
    def __init__(self,type,datasize,maxsize):
          self.type=type
          self.datasize=datasize
          self.maxsize=maxsize


    def  gettype(self):
        return self.type
    def  getdatasize(self):
        return self.datasize
    def getmaxsize(self):
        return self.maxsize


class flv(object):
    '''flv类型设计
      不做不行了，老师发火了
    '''


    def __init__(self,file_flv):
         self.file=open(file_flv,'rb')

         sig=self.file.read(SIG_SIZE)
         ver=self.file.read(HEADER_VERSION)
         has=self.file.read(HEADER_HAS)
         sz=self.file.read(HEADER_SIZE)
         self.flvheader=flv_header(sig,ver,has,sz)
         self.file.seek(HEADER_SIZE,io.SEEK_CUR)#JUM
#
#
#
#SIG_SIZE=0X3
#HEADER_VERSION=0X1
#HEADER_HAS=0X1
#HEADER_SIZE=0X4
#
# #
         meteversion=self.file.read(HEADER_VERSION)
         dsz=self.file.read(SIG_SIZE)
         timestamp=self.file.read(HEADER_SIZE)
         streamid=self.file.read(SIG_SIZE)

         dsz=bytearray(dsz)
         mete_sz=dsz[0]*math.pow(2,16)+dsz[1]*math.pow(2,8)+\
                 dsz[2]*math.pow(2,0)
         offset=mete_sz
         offset=int(offset)
         self.file.seek(offset+4,io.SEEK_CUR)#偏移位置
         #########开始判断##############
         #self.file.read(HEADER_VERSION)
    def  read_video_data(self):
         #read infomation
         type=self.file.read(HEADER_HAS)
         type_t=bytearray(type)
         type_t=type_t[0]
         if int(type_t)==9: #视频数据

             sz=self.file.read(SIG_SIZE)
             array_sz=bytearray(sz)
             sz=sz[0]*math.pow(2,16)+sz[1]*math.pow(2,8)+\
                     sz[2]*math.pow(2,0)
             sz=int(sz)
             tmstamp=self.file.read(HEADER_SIZE)
             streamid=self.file.read(SIG_SIZE)
             data=self.file.read(sz)
             self.file.seek(4, io.SEEK_CUR)
             return (sz,data)
             #rtmp = rtmp_package()
             #end
         #end information


    def  read_audio_data(self):
        # read infomation
        type = self.file.read(HEADER_HAS)
        type_t = bytearray(type)
        type_t = type_t[0]
        if int(type_t) == 8:  # 视频数据
            sz = self.file.read(SIG_SIZE)
            array_sz = bytearray(sz)
            sz = sz[0] * math.pow(2, 16) + sz[1] * math.pow(2, 8) + \
                 sz[2] * math.pow(2, 0)
            sz = int(sz)
            tmstamp = self.file.read(HEADER_SIZE)
            streamid = self.file.read(SIG_SIZE)
            data = self.file.read(sz)
            self.file.seek(4,io.SEEK_CUR)
            return (sz,data)


    def body(self):
        pass
    def getfile(self):
        return self.file
    def getflv_header(self):
        return self.flvheader
    def __del__(self):
        self.file.close()




#basic 1
#msg_head 11
#tmstamp 4
#data 128

import time

class msg_head(object):
    def __init__(self,tmstamp,msglength,msgid,msgstreamid):
         self.tmstamp=time.time()
         self.msgid=msgid
         self.msgstreamid=msgstreamid


import  random

import  os


''''
  rtmp package 的使用
 '''

class rtmp_package(object):
    def __init__(self,basic_head,msg_head,tmstamp,data,sz,type):
           self.basic_head=str(0b00000111)
           self.time_stamp=0x000000
           self.len=sz
           self.msgid=random.random(1024)
           self.msgtypy=type
           self.data=data

    def getbasic_head(self):
        return self.basic_head
    def getmsg_head(self):
        return self.msg_head
    def gettmstamp(self):
        return self.tmstamp
    def getdata(self):
        return  self.data

    def setbasic_head(self,basichead):
        self.basic_head=basichead
    def setmsg_head(self,msg):
        self.msg_head=msg
    def settmstamp(self,tmstamp):
        self.tmstamp=tmstamp
    def setdata(self,data):
        self.data=data

#rtmp chunk class
class rtmp_chunk(object):
    def __init__(self):
        pass

##rtmp connect
class csrtmp_conn(object):
    def __init__(self,addr,port):
        self.addr=addr
        self.port=port
        self.s=socket.socket()

    def rtmp_connect(self):
        self.s.connect((self.addr,self.port))

    def rtmp_send(self,data):
        self.s.send(data)
    def rtmp_recv(self):
        return self.rtmp_recv()
    def __del__(self):
        self.s.close()



if __name__ == '__main__':

         #m_flv=flv('test02.flv')
         conntect=csrtmp_conn('10.99.1.144',80)
         conntect.rtmp_connect()
         f=flv('test02.flv')
         while True:
             pass 




















