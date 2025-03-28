import sys
import os
import logging


class File_Manager():
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
        
        
    
file = File_Manager("C:\\Users\\amigo\\OneDrive\\Documentos\\Linux back up\\testdir1\\")
archivos_in = file.get_file_list()
file.delete_duplicate_file(archivos_in)
