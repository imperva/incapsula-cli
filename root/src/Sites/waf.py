from Sites.exception import IncapException
from Sites.uWaf import update
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class Security:
    def __init__(self, data, site_id):
        self.wafRuleList = []
        if 'waf' in data:
            waf_rule = {}
            for wafRules in data["waf"]["rules"]:
                logger.info('Add WAF rule name: {} to {}'.format(wafRules['name'], wafRules.get('action_text')))
                waf_rule['site_id'] = site_id
                waf_rule['rule_id'] = wafRules['id']
                if wafRules.get('action'):
                    waf_rule['security_rule_action'] = wafRules['action']
                if wafRules.get('exceptions'):
                    exception = IncapException(wafRules.get('exceptions'), site_id, waf_rule['rule_id'], wafRules['name'])
                    exception.update()
                if wafRules.get('block_bad_bots') is not None:
                    waf_rule['block_bad_bots'] = str(wafRules.get('block_bad_bots')).lower()
                if wafRules.get('challenge_suspected_bots') is not None:
                    waf_rule['challenge_suspected_bots'] = str(wafRules.get('challenge_suspected_bots')).lower()
                self.wafRuleList.append(waf_rule)
                waf_rule = {}

    def update(self):
        for rule in self.wafRuleList:
            update(rule)
