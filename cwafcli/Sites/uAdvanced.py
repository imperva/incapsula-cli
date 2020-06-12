from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.incapResponse import IncapResponse


def u_advanced(args):
    param = vars(args)
    output = 'Update advanced cache setting on {0}.'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        resp = IncapResponse(result)
        print('Updated advanced cache, set {} to {} on site ID: {}'
              .format(param.get('param').replace('_', ' '), param.get('value'), param.get('site_id')))
        resp.log()
        return resp


def update(params):
    resturl = 'sites/performance/advanced'
    if params:
        if "site_id" in params and "param" in params and "value" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id or (param : value) parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')