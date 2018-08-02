from Utils.executeRest import execute
from Utils.incapError import IncapError
from Utils.incapResponse import IncapResponse
import logging
import json


def d_site(args):
    output = 'Delete site ID = {0}!'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id
    }
    result = delete(param)
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        resp = IncapResponse(result)
        resp.log()
        return resp


def delete(params):
    resturl = '/api/prov/v1/sites/delete'

    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.error('No domain parameter has been passed in.')
    else:
        logging.error('No parameters where passed in.')
