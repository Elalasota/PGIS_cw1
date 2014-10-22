#!/usr/bin/env python
#-*- coding: utf-8 -*-

import math

def kwadratowa(a,b,c,x):
    return a*x**2+b*x+c

def delta(a,b,c):
    return b**2-4*a*c

def miejsca_zerowe(a,b,c):
    d = delta(a,b,c)
    if d>0:
        x1=(-float(b)-math.sqrt(d))/(2.0*float(a))
        x2=(-float(b)+math.sqrt(d))/(2.0*float(a))
        return (x1,x2)
    elif d<0:
        return None
    else:
        x=-b/(2*a)
        return (x)
    
print "Miejsca zerowe funkcji: "+str(miejsca_zerowe(1,-1,-1))
for i in xrange(-10, 11,1):
    print "Wartość funkcji dla podanego argumentu: "+str(kwadratowa(1,-1,-1,i))
