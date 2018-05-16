import logging

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\spoonath\\Documents\\MISC\\python_scripts\\my_git_python\\python\\python.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w'  # to overwrite old logs
                    )
logger = logging.getLogger()

logger.info('*'*25 + "  LOGS  " + '*'*25)
