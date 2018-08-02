from Utils.executeRest import execute
import Utils.log
from Accounts.account import Account
from Utils.incapError import IncapError
import json
import logging


def r_accounts(args):
    output = 'Get accounts!'
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "page_size": args.page_size,
        "page_num": args.page_num
    }
    result = read(param)
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        for accounts in result['accounts']:
            account = Account(accounts)
            print(account.log())


def read(params):
    resturl = '/api/prov/v1/accounts/list'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')