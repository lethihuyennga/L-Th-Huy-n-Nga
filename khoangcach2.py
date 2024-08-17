# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:36:58 2024

@author: le Thi Huyen Nga
"""

distance = float(input("Nhap do doi doan duowng den truong(m):"))
if distance <300:
    print("Duong den truong qua gan. Thoi! Di bo")
elif distance >1200:
    print("Duong den truong qua xa. Thoi! Di xe may")
elif distance >=300 and distance <=700:
    print("Duong den truong khong xa. Thoi! Di xe dap")
else:
    print("Khong xac dinh")