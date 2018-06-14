import time
from pprint import pprint

from Integration.clapps import r_clapps
import Utils.log
from Utils.incapError import IncapError
logger = Utils.log.setup_custom_logger(__name__, fmt='%(message)s')


class SubAccount:
    def __init__(self, data):
        self.sub_account_id = data.get('sub_account_id') or ''
        self.sub_account_name = data.get('sub_account_name') or ''
        self.support_level = data.get('support_level') or ''

    def log(self):
        divide = '-------------------------------------------------------------------------------------------------'
        logger.debug(divide)
        logger.debug('Sub Account Name: %s' % self.sub_account_name)
        logger.debug('Sub Account ID: %s' % self.sub_account_id)
        logger.debug('Support Level: %s' % self.support_level)
