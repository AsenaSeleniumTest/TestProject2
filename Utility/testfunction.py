# -*- coding: utf-8 -*-
import math
import os
import random
import re
import json
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
#Completar el ejercicio de sortear los caracteres
# Rank an array of integers 1 for highest and so forth add same rank for duplicates
# Count ip´addresses based on input ip address and rturn the number of ip addresses

def sort_code(code):
    """"""
    return "".join(sorted(code))

def rank_scores(scores):
	"""Rank an array of integers 1 for highest and so forth add same rank for duplicates"""	
	sorted_scores = sorted(scores,reverse=True)
	rank_dict = {score: rank + 1 for rank, score in enumerate(sorted_scores)}
	return [rank_dict[score] for score in  sorted_scores]

data = rank_scores([100, 90, 90, 80, 75, 60])
print(data)

def read_json_file():
        """ read data from json file"""
        os.chdir("..\\TestProject2\\Tests\\Data")
        try:
            with open("formdata.json","r") as f:
                data_1 = json.load(f)
                data_list = data_1["students"]
                return data_list
        except FileNotFoundError as file:
            return file
        
if __name__ == "__main__":
	
	file_data = read_json_file()
	print(file_data[1])