import logging

class CustomLogger:
    @staticmethod
    def log_generator():
        logging.basicConfig(filename='.\\logs\\testprojectInfo.log',  level=logging.INFO, force= True, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        return logger

