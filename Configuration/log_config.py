#!/usr/bin/env python3
import logging as Logger
import datetime as Datetime

class Log_Config():
    """Class to configure the logger"""
        
    @staticmethod
    def get_log():
        """Get the logger"""
        Logger.basicConfig(level=Logger.DEBUG,
                           format='%(asctime)s - %(levelname)s - %(message)s',
                           file=f"Logs\\testlogs\\test_log{Datetime.date}.log")
        return Logger.getLogger(__name__)

if __name__ == "__main__":
    print("This is a module for configuring the logger. ")
    log = Log_Config.get_log
    print(log.__code__)