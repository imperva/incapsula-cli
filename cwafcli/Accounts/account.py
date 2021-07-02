import time
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
               '\nAccount ID: %s\nTrial End Dates: %s\nSupport Level: %s\nSupport all TLS Versions: %s' \
               % (
                   self.plan_name, self.account_name, self.email, self.account_id, self.trial_end_date,
                   self.support_level,
                   self.support_all_tls_versions)

    @staticmethod
    def get_subscription(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/subscription".format(**param),
            param, body=param)

    @staticmethod
    def list_sub_account(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/accounts/listSubAccounts".format(**param),
            param, body=param)

    @staticmethod
    def audit(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        response = execute("https://api.imperva.com/audit-trail/v2/events",
            param, "GET", body=param)
        if param["output"] == "friendly":
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['context_key', 'type_description', 'user_details', "time"],
                data=response['elements'])
            from cwafcli.Utils.print_table import PrintTable
            return PrintTable(label='Audit', data=format_site.headers).print_all()
        else:
            return response

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
        response = execute("https://my.imperva.com/api/prov/v1/accounts/list".format(**param),
            param, body=param)
        if param["output"] == "friendly":
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['account_name', 'email', 'plan_name', "user_name"],
                data=response['accounts'])
            from cwafcli.Utils.print_table import PrintTable
            return PrintTable(label='Managed Accounts', data=format_site.headers).print_all()
        else:
            return response

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


class Audit:
    def __init__(self, data):
        self.createdAt = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(int(data.get('createdAt'))/1000.0)) or ''
        self.account_id = data.get('account_id') or ''
        self.user_id = data.get('user_id') or ''
        self.type_key = data.get('type_key') or ''
        self.type_description = data.get('type_description') or ''
        self.context = data.get('context') or ''
        self.response_message = data.get('res_message') or ''
        self.site_id = data.get('site_id') or ''
        self.changes = data.get('changes') or ''

    def log(self):
        return '-------------------------------------------------------------------------\n' \
               'Audit Details:\nTime: %s\nAccount ID: %s\nUser ID: %s\nDescription: %s' \
               '\nContext: %s\nChanges: %s' % (self.createdAt, self.account_id, self.user_id,
                                               self.type_description, self.context, self.changes)