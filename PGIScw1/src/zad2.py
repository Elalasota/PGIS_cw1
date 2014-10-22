#!/usr/bin/env python
#-*- coding: utf-8 -*-
print "zażółć gęślą jaźń"
def palindrom(lancuch):
    lancuch=lancuch.lower()
    lancuch=lancuch.replace(" ", "")
    print lancuch
    lancuch_odwrocony=lancuch[::-1]
    print lancuch_odwrocony
    if lancuch_odwrocony==lancuch:
        return True
    else:
        return False
print palindrom("Kobyła ma mały bok")    
print palindrom("Zakopane na pokaz")