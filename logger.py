import logging

logging.basicConfig(
    format = '%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename='logs.txt'
)
logger = logging.getLogger(__name__)
logger.info('This is an info logger')
logger.debug('this is a debug log')
logger.warning('this is a warning')
logger.error('this is an error log')
logger.critical('this is a critical error')