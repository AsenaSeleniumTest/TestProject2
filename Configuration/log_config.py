#!/usr/bin/env python3
import logging as Logger
from datetime import datetime



def get_debug_logger_():
    """Get the logger configuration"""
    path = f'Logs/testlogs/test_log{datetime.now()}.log'
    d_logger = Logger.getLogger(__name__)
    d_logger.setLevel(Logger.INFO)
    d_formater = Logger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    d_handler = Logger.FileHandler(path)
    d_handler.setFormatter(d_formater)
    d_logger.addHandler(d_handler)
    return d_logger

def get_critical_logger():
    """Get the logger configuration"""
    path = f'Logs/testlogs/error_log{datetime.now()}.log'
    c_logger = Logger.getLogger(__name__)
    c_logger.setLevel(Logger.CRITICAL)
    c_formater = Logger.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler = Logger.FileHandler(path)
    c_handler.setFormatter(c_formater)
    c_logger.addHandler(c_handler)
    return c_logger
   
if __name__ == "__main__":
    print("This is a module for configuring the logger. ")
    