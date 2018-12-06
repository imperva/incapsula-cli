import json
import os
from Utils.executeRest import execute
import logging
from Utils.incapError import IncapError


def get_clapps(cl_id):
    cl_id = cl_id[0]
    logging.debug('Retrieving client application name and application type for Client ID:{}.'.format(cl_id))
    param = {
        "api_id": None,
        "api_key": None
    }

    try:
        filename = os.path.expanduser('~') + '/.incap/exports/clapps.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if not os.path.isfile(filename):
            return get_update_file(filename, param, cl_id)
        with open(filename, 'r') as f:
            result = json.load(f)
        if cl_id in result['clientAppTypes']:
            return result['clientAppTypes'][cl_id] + ' with client name ' + result['clientApps'][cl_id]
        else:
            return get_update_file(filename, param, cl_id)
    except OSError as e:
        logging.error(e.strerror)


def get_update_file(filename, param, cl_id):
    try:
        with open(filename, 'w') as outfile:
            result = read(param)
            if int(result.get('res')) != 0:
                err = IncapError(result)
                err.log()
            else:
                json.dump(result, outfile)
                return result['clientAppTypes'][cl_id] + ' with client name ' + result['clientApps'][cl_id]
    except OSError as e:
        logging.error(e.strerror)


def read(param):
    resturl = '/api/integration/v1/clapps'
    return execute(resturl, param)

