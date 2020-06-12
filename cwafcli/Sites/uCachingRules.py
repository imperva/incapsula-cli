from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.incapResponse import IncapResponse


def u_cacherule(args):
    param = vars(args)
    output = 'Update cache rules on {0}.'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        resp = IncapResponse(result)
        print('Updated cache rule(s) on site ID: {}'.format(param.get('site_id')))
        for k, v in param.items():

            if len(k) > 10 and len(v) > 0:
                print('Setting {} to {}'.format(k.replace('_', ' '), v))
        resp.log()
        return resp


def update(params):
    resturl = 'sites/performance/caching-rules'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')