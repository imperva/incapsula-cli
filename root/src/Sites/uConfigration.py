from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging

from Utils.incapResponse import IncapResponse


def u_configuration(args):
    output = 'Update site {0} with configuration param={1} and value={2}.'. format(args.site_id, args.param, args.value)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "param": args.param,
        "value": args.value
    }
    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        resp = IncapResponse(result)
        print('Updated Site ID: {} {} configuration to {}'.format(args.site_id, args.param.replace('_', ' '), args.value))
        resp.log()
        return resp


def update(params):
    resturl = '/api/prov/v1/sites/configure'
    if params:
        if "param" in params and "value" in params:
            return execute(resturl, params)
        else:
            logging.warning("No (param : value) parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')