#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    even = n % 2 == 0
    if (not even) or (even and n >= 6 and n <= 20):
        print("Weird")
    if (even and n > 20) or (even and n >= 2 and n <= 5):
        print("Not Weird")
        
