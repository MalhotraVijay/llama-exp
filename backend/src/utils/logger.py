
import logging
import logging.config 


from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

# setup loggers
# For enabling info logs change the level to INFO in the logging.conf
logging.config.fileConfig(log_file_path, disable_existing_loggers=True)

def getLogger(name):
    # get root logger
    return logging.getLogger(name) 