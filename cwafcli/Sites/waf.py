from ..Integration.exception import IncapExceptions
from ..Sites.uWaf import update
import logging


class Security:
    def __init__(self, data, site_id):
        self.wafRuleList = []
        if 'waf' in data:
            waf_rule = {}
            for wafRules in data["waf"]["rules"]:
                print('--------------------------------------------------------------------------')
                print('Add WAF Rule: {} and set to {}'.format(wafRules['name'], (wafRules.get('action_text')
                                                              or wafRules.get('activation_mode_text'))))
                waf_rule['site_id'] = site_id
                waf_rule['rule_id'] = wafRules['id']
                if wafRules.get('action'):
                    waf_rule['security_rule_action'] = wafRules['action']
                if wafRules.get('exceptions'):
                    IncapExceptions(wafRules.get('exceptions'), site_id, waf_rule['rule_id'], wafRules['name'])
                if wafRules.get('block_bad_bots') is not None:
                    waf_rule['block_bad_bots'] = str(wafRules.get('block_bad_bots')).lower()
                if wafRules.get('challenge_suspected_bots') is not None:
                    waf_rule['challenge_suspected_bots'] = str(wafRules.get('challenge_suspected_bots')).lower()
                if wafRules.get('ddos_traffic_threshold'):
                    waf_rule['ddos_traffic_threshold'] = wafRules.get('ddos_traffic_threshold')
                if wafRules.get('activation_mode'):
                    waf_rule['activation_mode'] = wafRules.get('activation_mode').lower()
                self.wafRuleList.append(waf_rule)
                logging.debug('WAF Param: {}'.format(waf_rule))
                waf_rule = {}

    def update(self):
        for rule in self.wafRuleList:
            update(rule)
