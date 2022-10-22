from loguru import logger

logger.add('logg.log', format="{time} - {level} - {message}", \
            level='DEBUG', rotation='10 KB', compression='zip')


# logger.debug('Hello, World(debug)!')