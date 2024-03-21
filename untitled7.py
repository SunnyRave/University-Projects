# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 05:11:56 2023

@author: Sunit Ravi
"""

A=[6,4,2,9,2,8,6,5]

def unknown(A,l,r):
    if l>r:
        return -1000
    elif l==r:
        return A[l]
    else:
        q=l+(r-l//3)
        ansL=unknown(A,l,q)
        ansR = unknown(A,q+1,r)
        if ansL > ansR:
            return ansL
        else:
            return ansR

unknown(A,0,7)   