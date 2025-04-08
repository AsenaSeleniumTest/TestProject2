# -*- coding: utf-8 -*-
import math
import os
import random
import re
from sys import path
path.append("..\\TestProject2\\Pages") 

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
strArr = ["A:1","B:2","A:3","D:4","E:5","E:-6","D:7","H:8","C:9","B:10"]
array2=set(strArr)

def search_array(strArr):
    suma=0 
    key_list = []
    valor_list = []
    dic_values = {}
    resultado = []
    for i in strArr:
        key1 = i.split(":")     
        key_list.append (key1[0])
        valor_list.append(key1[1]) 
        dic_values[key1[0]] = int(key1[1])
    key_list2 =set(key_list)
    key_list2 = list(key_list2)
    key_list2.sort()
    print("key_list2: ",key_list2)      
    for i in range(len(key_list2)):
        for j in range(len(key_list)):
            if key_list2[i] == key_list[j]:
                suma = suma + int(valor_list[j])
                print("key: ",key_list[j]," valor: ",valor_list[j])
        resultado.append(str(key_list2[i])+":"+str(suma))        
        suma = 0 
        print("suma: ",suma)

    print("key_list: ",key_list)
    print("valor_list: ",valor_list)
    print("dic_values: ",dic_values)
    print("resultado: ",resultado)    
    return resultado   
               
                


    
print(search_array(strArr))


 