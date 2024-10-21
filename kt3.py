# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:44:57 2024

@author: PC
"""
def chan_am(n):
    return n%2==0 and n<0 
def kt(n ):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2==0:
        return 1
    else:
        return 0
def ktra():
    n=input("Nhập: ")
    if n.replace(".","",1 ).replace("-","",1 ).isdigit():
        n=float(n )
    if -89<=n<=90:
        return n
    print("Nhập lại: " )
    return ktra()
def can_bac(n,x):
    return n**(1/x )
def so_dao(n ):
    return str(n)[::-1 ]
import math 
def chinh_phuong(n):
    return math.sqrt(n)==int(math.sqrt(n ))
def nguyen_to(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def tich_so_le(*args ):
    tich=1 
    for i in args:
        if i%2!=0:
            tich*=i
    return tich 
def tong_nguyen_to(n):
    tong=0
    for i in range (2,n ): 
        if nguyen_to(i):
            tong+=i
    return tong
def tong_chinh_phuong(n):
    tong=0
    for i in range(1,n):
        if chinh_phuong(i):
            tong+=i
    return tong
def tong_uoc_duong(n):
    tong=0
    for i in range(1,n+1):
        if n%i==0:
            tong+=i
    return tong
def fib(n):
    a,b=0,1
    while a<n: 
        print(a,end=" ")        
        a,b=b,a+b
def chu_vi(a,b):
    return (a+b)*2
def dien_tich(a,b):
    return a*b
def ve_hcn(a,b):
    for i in range(a) :
        print("*"*b )
import math 
def tinh(*args,**kwargs):
    hinh= kwargs.get("hinh")
    tinh=kwargs.get("tinh")
    if hinh=="vuong":
        canh=args[0 ]
        return canh*4 if tinh=="cv" else canh*canh
    elif hinh=="tron":
        bk=args[0 ]
        return math.pi*2*bk if tinh=="cv" else math.pi*bk**2
    elif hinh=="chu_nhat":
        dai, rong=args
        return (dai+rong)*2 if tinh=="cv" else dai*rong
    else:
        return "Hình không hợp lệ "
    
        
        
