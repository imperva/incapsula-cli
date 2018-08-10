import json
import os

from Utils.executeRest import execute
import logging
from Utils.incapError import IncapError


def r_clapps():
    logging.debug('Retrieving client apps list for client_app_id to Client Application Name.')
    param = {
        "api_id": None,
        "api_key": None
    }

    result = read(param)
    try:
        home = os.path.expanduser('~')
        filename = home + '/.incap/exports'
        if not os.path.exists(filename):
            os.makedirs(filename)
        with open(filename + '/clapps.json', 'w') as outfile:
            json.dump(result, outfile)
    except OSError as e:
        logging.error(e.strerror)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        return result


def read(param):
    resturl = '/api/integration/v1/clapps'
    return execute(resturl, param)

