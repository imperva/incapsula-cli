from Utils.executeRest import execute
from Accounts.sub_account import SubAccount
from Utils.incapError import IncapError
import logging
import json


def r_subaccount(args):
    output = 'Get sub accounts!'
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

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        for accounts in result['resultList']:
            account = SubAccount(accounts)
            print(account.log())


def read(params):
    resturl = 'accounts/listSubAccounts'
    if params:
            return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')