#!/usr/bin/python3

import sys
import os

def prime(s):
    if s==1:
        return False
    for i in range(2, s):
        if s%i==0:
            return False
    return True

for i in range(2,50):
    if prime(i):
        print(i)
