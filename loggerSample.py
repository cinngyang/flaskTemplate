import logging 
logging.basicConfig(level=logging.INFO,filename='app.log', format='%(asctime)s %(message)s')

# 'application' code

logging.info('info message')
logging.debug('debug message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
