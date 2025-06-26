#!/usr/bin/env python3
import logging as Logger
import os
from datetime import datetime

today_date = datetime.now()
LOG_DATE = str(today_date.strftime("%Y_%m_%d_%H:%M:%S"))
os.chdir("Logs\\testlogs")
def get_debug_logger():
    """Get the logger configuration"""
    path = 'test_log.log'
    d_logger = Logger.getLogger(__name__)
    d_logger.setLevel(Logger.INFO)
    d_formater = Logger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
    d_handler = Logger.FileHandler(path,mode='a')
    d_handler.setFormatter(d_formater)
    d_logger.addHandler(d_handler)
    return d_logger

def get_critical_logger():
    """Get the logger configuration"""
    path = 'error_log.log'
    c_logger = Logger.getLogger(__name__)
    c_logger.setLevel(Logger.CRITICAL)
    c_formater = Logger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
    c_handler = Logger.FileHandler(path, mode='a')
    c_handler.setFormatter(c_formater)
    c_logger.addHandler(c_handler)
    return c_logger
   
if __name__ == "__main__":
    print("This is a module for configuring the logger. ")
    print(LOG_DATE)
    log = get_debug_logger()
    log.info("This is a debug log message.")
    l_err = get_critical_logger()
    l_err.critical("This is a critical log message.")