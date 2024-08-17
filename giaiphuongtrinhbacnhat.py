# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:21:22 2024

@author: le Thi Huyen Nga
"""

a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
if a == 0 and b == 0:
    print("phương trình có vô số nghiệm.")
elif a== 0 and b !=0:
    print("phương trình vô nghiệm.")
elif a !=0 and b!=0:
    print("phương trình có 1 nghiệm duy nhất X=", -b/a)
else:
    print("không hợp lệ!")
    