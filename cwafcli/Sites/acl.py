from ..Integration.exception import IncapExceptions
from ..Sites.uACL import update
import logging


class ACL:
    def __init__(self, data, site_id=None):
        self.aclRuleList = []
        if 'acls' in data:
            acl_rule = {}
            for aclRules in data['acls']['rules']:
                print('--------------------------------------------------------------------------')
                acl_rule['site_id'] = site_id
                acl_rule['rule_id'] = aclRules['id']
                if 'geo' in aclRules:
                    if 'countries' in aclRules['geo']:
                        acl_rule['countries'] = ','.join(aclRules['geo']['countries'])
                        print('Add Security Rule: {}: "{}"'.format(aclRules['name'], acl_rule['countries']))
                    if 'continents' in aclRules['geo']:
                        acl_rule['continents'] = ','.join(aclRules['geo']['continents'])
                        print('Add Security Rule: {}: "{}"'.format(aclRules['name'], acl_rule['continents']))

                if 'urls' in aclRules:
                    urls = list([])
                    url_patterns = list([])
                    for url in aclRules['urls']:
                        urls.append(''.join(url['value']))
                        url_patterns.append(''.join(url['pattern']))
                        print('Add Security Rule: {}: "URL={}, PATTERN={}"'
                              .format(aclRules['name'], ''.join(url['value']), ''.join(url['pattern'])))
                    acl_rule['urls'] = ','.join(urls)
                    acl_rule['url_patterns'] = ','.join(url_patterns)

                if 'ips' in aclRules:
                    acl_rule['ips'] = ','.join(aclRules['ips'])
                    print('Add Security Rule: {}: "{}"'.format(aclRules['name'], acl_rule['ips']))

                if 'exceptions' in aclRules:
                    IncapExceptions(aclRules.get('exceptions'),
                                    site_id, acl_rule['rule_id'], aclRules['name'])
                self.aclRuleList.append(acl_rule)
                logging.debug('ACL Param: {}'.format(acl_rule))
                acl_rule = {}

    def update(self):
        for rule in self.aclRuleList:
            update(rule)
