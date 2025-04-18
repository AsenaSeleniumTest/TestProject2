import sys
import os
from os import strerror
import logging


class File_Manager():
    """ Class to handle read and write operations on files """
    def __init__(self,directorypath):
        self.directory=directorypath

    def get_file_list(self):
        try:
            files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory,f))]
        except FileNotFoundError as ex:
            logging.critical(f"Directory not found : {ex.__str__}" )
        except PermissionError as exp:     
            logging.critical(f"Directory Permission denied : {ex.__str__}" )
        return files
    
    def delete_duplicate_file(self,file_list):
        data_set = set(file_list)
        try:
            if data_set in file_list:
                print(f"trying to delete: {data_set}")
                os.remove(self.directory+data_set)
        except FileNotFoundError as ferror:       
            return ferror
        except PermissionError as exp:
            logging.critical(f"Directory Permission denied : {exp.__str__}" )
            return exp
            
        
    def read_file(self,filename):
        """ Read file content"""
        try:
            with open(filename,'r',encoding="UTF-8") as file:
                data1 = file.read()
                return data1
        except FileNotFoundError as ferror:   
            return ferror 
    def read_file_per_line(self,filename):
        """ Read file content line by line """
        try:
            with open(filename,'r',encoding="UTF-8") as file:
                data1 = file.readlines()
                return data1
        except FileNotFoundError as ferror:   
            return ferror      
    
    def write_file(self,filename,data):
        """ Write data to file """
        try:
            with open(filename,'w',encoding="UTF-8") as file:
                file.write(data)
        except FileNotFoundError as ferror:   
            return ferror
        
    def append_to_file(self,filename,data):
        """Append data to existing file"""
        try:
            with open(filename,'a',encoding="UTF-8") as file:
                file.write(data)
        except FileNotFoundError as ferror:   
            return ferror
    def read_update_file(self,filename,data=""):
        try:
            with open(filename,'r+',encoding="UTF-8") as file:
                file.write(data)
        except FileNotFoundError as ferror:   
            return ferror
    def write_update_file(self,filename,data=""):
        try:
            with open(filename,'w+',encoding="UTF-8") as file:
                file.write(data)
        except FileNotFoundError as ferror:   
            return ferror
    

"""fm = File_Manager
data = fm.read_file_per_line(fm,filename = f"{os.curdir}\\Utility\\network1.txt")
count = 0
for car in range(len(data)):
    #print(data[car],end="")
    count +=1
print(len(data))
print(f"total caracters in file : {count}")
    """
 
