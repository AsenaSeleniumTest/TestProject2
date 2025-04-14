#!/usr/bin/env python3
import logging as Logger
import datetime as Datetime
Logger.basicConfig(filename=f"Logs/testlogs/test_log{Datetime.date}.log",  # Log file name
            level=Logger.INFO,  # Logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
            format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
            datefmt="%Y-%m-%d %H:%M:%S",
            filemode="w")
logger = Logger.getLogger(__name__)
logger.setLevel(Logger.INFO)
stream_handler = Logger.StreamHandler()
stream_formatter = Logger.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger.addHandler(stream_handler)
file_handler = Logger.FileHandler(f"Logs/testlogs/test_log{Datetime.date}.log")
logger.addHandler(file_handler)

class log_filter(Logger.Filter):
    def filter(self, record: Logger.LogRecord):
        return record.levelno >= Logger.WARNING
logger.addFilter(log_filter())



        