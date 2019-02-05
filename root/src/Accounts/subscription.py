from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging
from Utils.reseller_usage import ResellerExport
import json


def r_subscription(args):
    output = 'Get account status!'
    param = vars(args)
    #action = param['do']
    #print('{} site data centers.'.format(str.capitalize(action)))
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
    logging.info(output)
    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "account_id": args.account_id
    # }
    excel = ResellerExport("data.xlsx")
    excel.add_header()
    accounts = []
    print(param)
    print(args.reseller)
    if bool(param["reseller"]):
        page = 0
        param['page_size'] = 5
        while True:
            param['page_num'] = page
            from Accounts.rAccounts import read
            results = read(param)

            if int(results.get('res')) != 0:
                err = IncapError(results)
                err.log()
                return err
            elif results["accounts"]:
                accounts.append(results)
                page += 1
                if page > 2:
                    break
            else:
                break
        # print(accounts)

        account_list = []
        for account in accounts:
            for sub_account in account["accounts"]:
                print(sub_account["account_id"])
                param["account_id"] = sub_account["account_id"]
                sub_account["bandwidthHistory"] = get(param).get("bandwidthHistory")
                print(sub_account)
                exit(0)
                account_list.append(get(param))
        excel.add_account_data(account_list)
        excel.add_account_info(accounts)
        excel.workbook.close()
        return
    else:
        result = get(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    # else:
    #     print(result)


def get(params):
    resturl = 'accounts/subscription'
    if params:
        return execute(resturl, params)
    else:
        logging.error('No parameters where passed in.')

# def get_account_ids(results):
#     for account in results["accounts"]:
#         accounts.append(account["account_id"])
#     print(accounts)
#     print(len(accounts))