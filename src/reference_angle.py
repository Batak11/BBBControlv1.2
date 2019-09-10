#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:27:34 2019

@author: rohatyildiz
"""


def reference_angle():
    ref_angle = int(input("What Reference Angle Would You like? "))
    if ref_angle < 0:
        ref_angle = 0
    elif ref_angle > 180:
        ref_angle = 180
    print(ref_angle)
    return(ref_angle)
