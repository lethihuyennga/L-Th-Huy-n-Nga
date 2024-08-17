# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:34:52 2024

@author: le Thi Huyen Nga
"""

import math
a =float(input("Nhập a:"))
b =float(input("Nhập b:"))
c =float(input("Nhập c:"))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép x = {x}", x)
else:
    x1 = -b + math.sqrt(delta) / (2*a)
    x2 = -b - math.sqrt(delta) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt x1 = {x1}, x2 = {x2}")
    print("x1:", x1)
    print("x2:", x2)
    