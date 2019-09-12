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


def output_cut(output):
    if output > 1:
        output = 1
    elif output < -1:
        output = 0
    return output


def output_mapped(output_cut):
    mapped_output = 50+50*output_cut
    return mapped_output
