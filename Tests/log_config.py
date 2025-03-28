import logging as Logger

Logger.basicConfig(filename="test_log.log",  # Log file name
            level=Logger.INFO,  # Logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
            format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
            datefmt="%Y-%m-%d %H:%M:%S",
            filemode="w")
logger = Logger.getLogger()