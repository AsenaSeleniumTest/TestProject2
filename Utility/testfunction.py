# -*- coding: utf-8 -*-
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    for val in range(len(ar)):
        for data in range(1,len(ar)):
            if ar[val] == ar[data]:
                pair_count +=1
                val +=1
                data+=1
                continue     
                
    return pair_count

print(sockMerchant(9,[10,20,20,10,10,30,50,10,20]))