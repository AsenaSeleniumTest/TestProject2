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
# git init.
# git add -A.
# git commit -m 'Added my project'
# git tag "add tag version"
# git push --tags 
# git remote add origin git@github.com: sammy/my-new-project.git.
# git push -u -f origin main.
#

def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    for val in range(len(ar)):
        for data in range(1,len(ar)):
            if ar[val] == ar[data]:
                pair_count +=1
                ar.remove(ar[val])
                ar.remove(ar[data])
                sockMerchant(n,ar) # recursive call to remove the pairs    
                continue     
                
    return pair_count




 