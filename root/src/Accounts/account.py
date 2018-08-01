import time
from pprint import pprint

from Integration.clapps import r_clapps
import Utils.log
from Utils.incapError import IncapError
logger = Utils.log.setup_custom_logger(__name__, fmt='%(message)s')


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
               % (self.plan_name, self.account_name,self.email, self.account_id, self.trial_end_date, self.support_level,
                  self.support_all_tls_versions)
