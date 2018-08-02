import logging


def setup_custom_logging(name, fmt='%(levelname)s - Module:(%(module)s) - %(message)s',
                        loglevel=logging.DEBUG):
    formatter = logging.Formatter(fmt=fmt)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging = logging.getlogging(name)
    logging.setLevel(loglevel)
    logging.addHandler(handler)
    return logging
