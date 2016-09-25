# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:37:38 2016

@author: Administrator
"""
import os
import time
a=(" ######       ##        ##        #####")
b=(" #           #  #      #  #       #    #")
c=(" #  ###     #    #    #    #      #     #")
d=(" #    #    #      #  #      #     #    #")
e=(" ######   #        ##        #    #####")
h=("\n")
j=(" ")
i=1
while i<20:
    print(a+h+b+h+c+h+d+h+e+h)
    time.sleep(0.5)
    i=i+1
    a=j+a
    b=j+b
    c=j+c
    d=j+d
    e=j+e
    
    os.system('cls')
    
input("please Enter:")
