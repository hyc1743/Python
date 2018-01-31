#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h=input('height: ')
w=input('weight: ')
height=float(h)
weight=float(w)
bmi=weight/(height*2)
if bmi<19.5:
    print('overlight')
elif bmi>=18.5 and bmi<=25:
    print('normal')
elif bmi>25 and bmi<=28:
    print('overweight')
elif bmi>28 and bmi<=32:
    print('fat')
else:
    print('overfat')
