from ..Utils.executeRest import execute
from ..Accounts.account import Account
from ..Utils.incapError import IncapError
import logging


def r_account(args):
    output = 'Get account status!'
    param = vars(args)
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
    logging.info(output)

    result = read(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        account = Account(result)
        print(account.log())


def read(params):
    resturl = 'account'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')
