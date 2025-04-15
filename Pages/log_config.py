#!/usr/bin/env python3
import logging as Logger
import datetime as DateTime
Logger.basicConfig(filename=f"Logs\\testlogs\\page_log{DateTime.date}.log",  # Log file name
            level=Logger.INFO,  # Logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
            format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
            datefmt="%Y-%m-%d %H:%M:%S",)
logger = Logger.getLogger()