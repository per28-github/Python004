#!/usr/bin/env python
#coding:utf-8
import threading
import time
 
mutex = threading.RLock()
state = [0,0,0,0,0]
 
rlock0 = threading.RLock()
rlock1 = threading.RLock()
rlock2 = threading.RLock()
rlock3 = threading.RLock()
rlock4 = threading.RLock()
  
class Phd():
    def __init__ (self,key,left,right,lock):
        self.key = key
        self.left = left
        self.right = right
        self.lock = lock
 
z1 = Phd(0,1,4,rlock0)
z2 = Phd(1,0,2,rlock1)
z3 = Phd(2,1,3,rlock2)
z4 = Phd(3,2,4,rlock3)
z5 = Phd(4,3,0,rlock4)
 
obj_Phd_list = [z1,z2,z3,z4,z5]
inter = 0
def take_forks(zname):
    global inter
    while 1:
        inter += 1
        key =  zname.key
        mutex.acquire()
        state[key] = 1
        res = test(zname)
        mutex.release()
        if res == 1:
            print ("----",zname.key,"hava eating----")
            print ("----" ,zname.key,"put forks")
            put_forks(zname)
        else:
            print("----",zname.key,"no forks")
            zname.lock.acquire()
        if (inter >= 30):
            break
def test(i):
    print(i.key,"--in the test")
    if (state[i.key] == 1 & state[i.left] !=2 & state[i.right] != 2):
        state[i.key] = 2
        try:
            i.lock.release()
        except:
            pass
        return 1
    return 0
 
def put_forks(i):
    mutex.acquire()
    state[i.key] = 0
    test(obj_Phd_list[i.right])
    test(obj_Phd_list[i.left])
    mutex.release()
 
 
 
for i in range(5):
    s =  threading.Thread(target=take_forks,args=(obj_Phd_list[i],))
    s.start()