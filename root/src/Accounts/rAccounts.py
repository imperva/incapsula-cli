from Utils.executeRest import execute
from Accounts.account import Account
from Utils.incapError import IncapError
import logging


def r_accounts(args):
    output = 'Get accounts!'
    param = vars(args)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "account_id": args.account_id,
    #     "page_size": args.page_size,
    #     "page_num": args.page_num
    # }
    result = read(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        for accounts in result['accounts']:
            account = Account(accounts)
            print(account.log())


def read(params):
    resturl = 'accounts/list'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')
