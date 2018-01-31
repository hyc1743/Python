# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    d=b*b-(4*a*c)
    if d>=0:
        r1=(-b + math.sqrt(d))/(2*a)
        r2=(-b - math.sqrt(d))/(2*a)
        return r1,r2
    else:
        return 'Wrong numbers'
a=float(input('Please input a= '))
b=float(input('Please input b= '))
c=float(input('Please input c= '))
print(quadratic(a,b,c))

