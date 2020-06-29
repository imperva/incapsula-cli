from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging

from ..Utils.incapResponse import IncapResponse


def d_certificate(args):
    param = vars(args)
    #action = param['do']
    output = 'Delete Certificate to: {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "site_id": args.site_id
    # }

    result = delete(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        resp = IncapResponse(result)
        print('Deleted certificate from site ID: {}'.format(args.site_id))
        resp.log()
        return resp


def delete(params):
    resturl = 'sites/customCertificate/remove'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')