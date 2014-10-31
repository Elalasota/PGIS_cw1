#!/usr/bin/env python
#-*- coding: utf-8 -*-
def palindrom(lancuch):
    lancuch=lancuch.lower().replace(" ", "").decode("utf-8")
    lancuch_odwrocony=lancuch[::-1]
    if lancuch_odwrocony==lancuch:
        return True
    else:
        return False
print palindrom("Kobyła ma mały bok")    
print palindrom("Zakopane na pokaz")
print palindrom("Cokolwiek")