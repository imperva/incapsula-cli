from Utils.executeRest import execute
from Accounts.account import Account
from Utils.incapError import IncapError
import logging
import json


def r_account(args):
    output = 'Get account status!'
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    logging.info(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id
    }
    result = read(param)
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        account = Account(result)
        print(account.log())


def read(params):
    resturl = '/api/prov/v1/account'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')
