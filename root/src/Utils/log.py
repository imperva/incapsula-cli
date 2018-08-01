import logging


def setup_custom_logger(name, fmt='%(levelname)s - Module:(%(module)s) - %(message)s',
                        loglevel=logging.DEBUG):
    formatter = logging.Formatter(fmt=fmt)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(loglevel)
    logger.addHandler(handler)
    return logger
