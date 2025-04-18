import os
import pytest
from Utility.file_manager import File_Manager

#@pytest.mark.filemanager
def s_test_readfile():
    fm=File_Manager
    data = fm.read_file(fm,filename="./Utility/network1.txt")
    for d in data:
        print(d)
    os.environ["network"]=data