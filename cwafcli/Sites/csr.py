from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
import base64
from ..Utils.incapResponse import IncapResponse


def new_csr(args):
    param = vars(args)
    #action = param['do']
    output = 'New CSR request for: {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    result = request(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        print('Certificate Request: {} '.format(result['csr_content']))
        return True


def request(params):
    resturl = 'sites/customCertificate/csr'
    if params:
        logging.debug(params)
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
