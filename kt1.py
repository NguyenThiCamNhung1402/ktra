# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:50:25 2024

@author: PC
"""
#1
def tong_chu_so(n ):
    if n>0:
        hangchuc=n//10
        hangdonvi=n%10
        tong= hangchuc+hangdonvi
        return tong 
    else:
        return n
#5 
def doi_giay():
    h,m,s=map(int,input("Nhập hh:mm:ss ").split(":"))
    doi_giay=h*3600+m*60+s
    return doi_giay
#10 
def so_nut(n ):
    while n>=10:  
        n=sum(int(i) for i in str(n))
    return n
#16
def doi_giay2():
    n= input("Nhập vd 1h8p8s ")
    h,m,s  = map(int,n.replace("h"," ").replace("p"," ").replace("s"," " ).split()) 
    doi_giay=h*3600+m*60+s 
    return doi_giay 
#18 
#21
def doc(n ):
    ds=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
    if 0<=n<=9:
        return ds[n]
    else:
        return "Không đọc được "
#22
def pt_bac_nhat(a,b):
    if a==0 and b==0:
        return "Phương trình vô số nghiệm "
    elif a==0 and b!=0:
        return "Phương trình vô nghiệm "
    else:
        return -b/a
#23
def pt_bac_hai(a,b,c ):
    if a<=0 or b<=0:
        return "a,b phải lớn hơn 0"
    else:
        delta=b**2-4*a*c
        if delta<0:
            return "Pt vô nghiệm "
        elif delta == 0:
            return -b/(2*a) 
        else:
            x1= (-b-(delta**0.5 ))/(2*a) 
            x2= (-b+(delta**0.5 ))/(2*a) 
            return x1, x2
#24
def ktr_gio(h,m,s ):
    if 0<=h<24 and 0<=m<60 and 0<=s<60 :
        return "hợp lệ "
#25 
def doi_kieu():
    n= input("nhập: ")
    if n.islower():
        n=n.upper()
    else:
        n=n.lower()
    return n
#26a
def tang_dan(a,b,c  ): 
    return sorted([a,b,c])
def giam_dan(a,b,c ):
    return sorted([a,b,c ],reverse=True )
#26b
def sap_xep(n ):
    n=str(n )
    sx=''.join(sorted(n ))
    return sx 

