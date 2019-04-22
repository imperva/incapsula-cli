from Accounts.account import Account
from Utils.executeRest import execute
import logging
import json
from Utils.incapError import IncapError


def c_account(args):
    output = 'With API_ID{0}, API Key={1} lets add {2}!'. format(args.api_id, args.api_key, args.account_name)
    param = vars(args)
    #action = param['do']
    #print('{} site data centers.'.format(str.capitalize(action)))
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
    logging.info(output)

    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "email": args.email,
    #     "parent_id": args.parent_id,
    #     "ref_id": args.ref_id,
    #     "user_name": args.user_name,
    #     "plan_id": args.plan_id,
    #     "log_level": args.log_level,
    #     "logs_account_id": args.logs_account_id,
    #     "account_name": args.account_name
    # }
    result = create(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        account = Account(result)
        print(account.log())


def create(params):
    resturl = 'accounts/add'
    if params:
        if "email" in params:
            return execute(resturl, params)
        else:
            logging.warning("No email parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
