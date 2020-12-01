import json
import logging
from ..Utils.executeRest import execute


class Account:
    def __init__(self, data):
        self.email = data.get('email') or ''
        self.plan_id = data.get('plan_id') or ''
        self.plan_name = data.get('plan_name') or ''
        self.trial_end_date = data.get('trial_end_date') or ''
        self.account_id = data.get('account_id') or int
        self.res = data.get('res') or int
        self.response_message = data.get('res_message') or ''
        self.ref_id = data.get('ref_id') or int
        self.user_name = data.get('user_name') or ''
        self.account_name = data.get('account_name') or ''
        self.support_level = data.get('support_level') or ''
        self.support_all_tls_versions = str(data.get('support_all_tls_versions')) or ''

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Plan Name: %s\nAccount Name: %s\nAccount Admin Email: %s' \
               '\nAccount ID: %s\nTrial End Dates: %s\nSupport Level: %s\nSupport all TLS Versions: %s'\
               % (self.plan_name, self.account_name, self.email, self.account_id, self.trial_end_date, self.support_level,
                  self.support_all_tls_versions)

    @staticmethod
    def get_subscription(args, ctx: dict):
        param = {**vars(args), **ctx}
        logging.info('Subscription Response: {}'.format(json.dumps(execute(param["do"], param), indent=4)))

    @staticmethod
    def list_subaccount(args):
        param = args
        accounts = execute(param["do"], param)
        for account in accounts["resultList"]:
            print('-------------------------------------------------------------------------------------------------\n'
                  'Sub Account Name: %s\nSub Account ID: %s\nSupport Level: %s' % (account["sub_account_name"],
                                                                                   account["sub_account_id"],
                                                                                   account["support_level"]))

    @staticmethod
    def create(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/add".format(**param),
                       param, body=param)

    @staticmethod
    def read(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/account".format(**param),
                       param, body=param)

    @staticmethod
    def update(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/configure".format(**param),
                       param, body=param)

    @staticmethod
    def list(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/list".format(**param),
                       param, body=param)

    @staticmethod
    def delete(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/delete".format(**param),
                       param, body=param)

class SubAccount:
    def __init__(self, data):
        self.sub_account_id = data.get('sub_account_id') or ''
        self.sub_account_name = data.get('sub_account_name') or ''
        self.support_level = data.get('support_level') or ''

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Sub Account Name: %s\nSub Account ID: %s\nSupport Level: %s' \
               % (self.sub_account_name, self.sub_account_id, self.support_level)

