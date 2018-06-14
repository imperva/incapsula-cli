from Sites.exception import IncapException
from Sites.uACL import update
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class ACL:
    def __init__(self, data, site_id=None):
        self.aclRuleList = []
        if 'acls' in data:
            acl_rule = {}
            for aclRules in data['acls']['rules']:
                logger.info('Add Security rule: {}'.format(aclRules['name']))
                acl_rule['site_id'] = site_id
                acl_rule['rule_id'] = aclRules['id']
                if 'geo' in aclRules:
                    if 'countries' in aclRules['geo']:
                        acl_rule['countries'] = ','.join(aclRules['geo']['countries'])
                    if 'continents' in aclRules['geo']:
                        acl_rule['continents'] = ','.join(aclRules['geo']['continents'])

                if 'urls' in aclRules:
                    urls = list([])
                    url_patterns = list([])
                    for url in aclRules['urls']:
                        urls.append(''.join(url['value']))
                        url_patterns.append(''.join(url['pattern']))
                    acl_rule['urls'] = ','.join(urls)
                    acl_rule['url_patterns'] = ','.join(url_patterns)

                if 'ips' in aclRules:
                    acl_rule['ips'] = ','.join(aclRules['ips'])

                if 'exceptions' in aclRules:
                    exception = IncapException(aclRules.get('exceptions'),
                                               site_id, acl_rule['rule_id'], aclRules['name'])
                    exception.update()
                self.aclRuleList.append(acl_rule)
                acl_rule = {}

    def update(self):
        for rule in self.aclRuleList:
            update(rule)
