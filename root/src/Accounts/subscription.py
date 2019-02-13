import time

from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging
from Utils.reseller_usage import ResellerExport


def r_subscription(args):
    output = 'Get account status!'
    param = vars(args)
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
    logging.info(output)

    excel = ResellerExport("data.xlsx")
    excel.add_header()
    accounts = []
    print(param)
    print(args.reseller)
    startTime = time.time()
    if bool(param["reseller"]):
        page = 0
        param['page_size'] = 100
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
                if page > 100:
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
                account_list.append(sub_account)
            # print(account_list)
            # exit(0)
        excel.add_account_data(account_list)
        excel.workbook.close()
        endTime = time.time()
        print("X transactions took: {}s".format(endTime - startTime))
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