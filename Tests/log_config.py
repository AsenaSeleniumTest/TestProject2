#!/usr/bin/env python3
import logging as Logger
import datetime as Datetime
Logger.basicConfig(filename=f"Logs\\testlogs\\test_log{Datetime.date}.log",  # Log file name
            level=Logger.INFO,  # Logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
            format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
            datefmt="%Y-%m-%d %H:%M:%S",
            filemode="w")
logger = Logger.getLogger(__name__)




        