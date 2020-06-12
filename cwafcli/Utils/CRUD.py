import logging


def create(params, resturl):
    resturl = 'accounts/add'
    if params:
        if "email" in params:
            return execute(resturl, params)
        else:
            logging.warning("No email parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')