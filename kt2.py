# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:59:54 2024

@author: PC
"""

#29
def tong_chu_so(n ):
    tong=0
    for i in str(n) :
        tong+= int(i )
    return tong 
#30
def bn_ngay(thang, nam ):
    nam_nhuan=(nam%4==0 and nam%100!=0 ) or (nam%400==0 )
    if thang in [1,3,5,7,8,10,12 ]:
        ngay=31
    elif thang in [4,6,9,11 ]:
        ngay=30
    elif thang ==2:
        ngay=29 if nam_nhuan else 28
    return ngay
#31
def tam_giac(a,b,c ):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a**2+b**2 == c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
                return "Tam giác vuông "
            elif a==b==c:
                return "Tam giác đều "
            elif a==b or b==c or a==c:
                return "Tam giác cân "
            else:
                return "Tam giác thường "
        else:
            return "Không tạo nên tam giác "
#32
def tinh_tien(n ):
    tong=0
    if n<=1:
        tong+= 15000
    elif 2<=n<=5:
        tong+= 15000 +(n*13500 )
    else:
        tong+= ((5*13500 )+ (n-5 )*11000 ) 
    if n>120:
        tong *= 0.9
    return tong
