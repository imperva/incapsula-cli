from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging

from ..Utils.incapResponse import IncapResponse


def u_configuration(args):
    output = 'Update site {0} with configuration param={1} and value={2}.'. format(args.site_id, args.param, args.value)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    param = vars(args)
    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        resp = IncapResponse(result)
        print('Updated Site ID: {} {} configuration to {}'.format(args.site_id, args.param.replace('_', ' '), args.value))
        return resp


def update(params):
    resturl = 'sites/configure'
    if params:
        if "param" in params and "value" in params:
            return execute(resturl, params)
        else:
            logging.warning("No (param : value) parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')