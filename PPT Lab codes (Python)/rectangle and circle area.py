#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:

    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r*self.r

if __name__ == '__main__': 
    r=Rectangle(4,7)
    c=Circle(7)
    print(r.area())
    print('%0.2f'%c.area()) 