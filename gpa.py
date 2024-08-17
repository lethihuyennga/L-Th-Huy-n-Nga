# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:46:17 2024

@author: Le Thi Huyen Nga
"""

GPA =float(input("Nhập Điểm trung bình GPA:"))
if GPA < 3.5:
    print("Học lực kém.")
elif 3.5<= GPA <= 5:
    print("Học lực yếu ")
elif 5.0<= GPA <7.0:
    print("Học lực trung bình.")
elif 7.0<= GPA <8.0:
    print("Học lực khá.")
elif 8.0<= GPA <9.0:
    print("Học lực giỏi.")
elif 9.0<= GPA <=10.0:
    print("Học lực xuất sắc.")