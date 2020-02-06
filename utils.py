import logging


def get_logger(name):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s [%(asctime)s] %(name)s %(message)s'
    )
    logger = logging.getLogger(name)
    return logger
