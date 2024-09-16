import logging

LOG_LEVEL_INFO = logging.INFO
LOG_LEVEL_DEBUG = logging.DEBUG
LOG_LEVEL_CRIT = logging.CRITICAL
LOG_LEVEL_ERROR = logging.ERROR
LOG_LEVEL_WARN = logging.WARNING


class LOGGER:
    @staticmethod
    def init(LoggerName: str, log_level, log_file: str):
        # Create a logger object
        logger = logging.getLogger('AppLogger')
        logger.setLevel(log_level)
        
        # Create a file handler for logging to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        
        # Create a console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        
        # Create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
