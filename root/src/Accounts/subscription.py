from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging


def r_subscription(args):
    output = 'Get account subscription!'
    param = vars(args)
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
    logging.info(output)

    result = read(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        print(result)


def read(params):
    resturl = 'accounts/subscription'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')
