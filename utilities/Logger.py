from datetime import datetime
import logging

class Logger:
    @staticmethod
    def get_logger():
        logging.basicConfig(filename=r'.\logs\automation.log',
                 encoding='utf-8',
                 level=logging.INFO,
                 force=True,
                 format='%(asctime)s %(message)s',
                 datefmt='%m%d%y %I:%M:%S %p')
        return logging.getLogger()