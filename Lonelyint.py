#!/bin/python3

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i
        
                

if __name__ == '__main__':
    n = int(input("Enter the number of integers in the array: ").strip())

    a = list(map(int, input("Enter the space-separated integers: ").rstrip().split()))

    result = lonelyinteger(a)

    print("The unique element is:", result)
