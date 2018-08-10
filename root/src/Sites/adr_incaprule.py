from Sites.cIncapRule import create
from Sites.dIncapRule import delete
from Sites.uIncapRule import update
import logging


class ADRuleRedirect:
    def __init__(self, data):
        self.to = data['to']
        self.id = data['id']
        self.enabled = data['enabled']
        self.priority = data['priority']
        self.response_code = data['response_code']
        self.last_7_days_requests_count = data['last_7_days_requests_count']
        self.name = data['name']
        self.action = data['action']
        self._from = data['from']
        self.filter = data['filter']

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Rule ID: %s -- Rule Name: %s\n' \
               '--to="%s" --from="%s" --name="%s" --response_code="%s"' \
               ' --filter="%s" --action=%s'\
               % (self.id, self.name, self.to, self._from, self.name, self.response_code,
                  self.filter, self.action)


class ADRuleRewrite:
    def __init__(self, data):
        self.to = data['to']
        self.id = data['id']
        self.enabled = data['enabled']
        self.priority = data['priority']
        self.add_missing = str(data.get('add_missing'))
        self.last_7_days_requests_count = data['last_7_days_requests_count']
        self.name = data['name']
        self.action = data['action']
        self._from = data['from']
        self.filter = data['filter']
        self.allow_caching = str(data.get('allow_caching'))
        self.rewrite_name = data['rewrite_name']

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Rule ID: %s -- Rule Name: %s\n' \
               '--to="%s" --from="%s" --name="%s" --rewrite_name="%s" --allow_caching=%s' \
               ' --add_missing=%s --filter="%s" --action=%s'\
               % (self.id, self.name, self.to, self._from, self.name, self.rewrite_name,
                  self.allow_caching, self.add_missing, self.filter, self.action)


class ADRuleForward:
    def __init__(self, data):
        self.id = data['id']
        self.enabled = data['enabled']
        self.priority = data['priority']
        self.last_7_days_requests_count = data['last_7_days_requests_count']
        self.name = data['name']
        self.action = data['action']
        self.dc_id = data['dc_id']
        self.filter = data['filter']
        self.allow_caching = str(data.get('allow_caching'))

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Rule ID: %s -- Rule Name: %s\n' \
               '--name="%s" --dc_id="%s"' \
               ' --allow_caching=%s --filter="%s" --action=%s'\
               % (self.id, self.name, self.name, self.dc_id,
                  self.allow_caching, self.filter, self.action)


class IncapRule:
    def __init__(self, data):
        if 'filter' in data:
            self.id = data['id']
            self.name = data['name']
            self.filter = data['filter']
            self.action = str.upper(data['action'].replace('api.rule_action_type.', ''))
        elif 'rule' in data:
            self.id = data['id']
            self.name = data['name']
            self.filter = data['rule']
            self.action = str.upper(data['action'].replace('api.rule_action_type.', ''))

    def set_param(self, site_id):
        return {
            "api_id": None,
            "api_key": None,
            "site_id": site_id,
            "name": self.name,
            "action": self.action,
            "filter": self.filter,
            "response_code": '',
            "protocol": '',
            "add_missing": '',
            "from": '',
            "to": '',
            "rewrite_name": '',
            "dc_id": '',
            "is_test_mode": '',
            "lb_algorithm": ''
        }

    @staticmethod
    def create_incap_rule(param):
        print('Create IncapRule: {}'.format(param['name']))
        logging.debug('IncaRule Param: {}'.format(param))
        create(param)

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               "Rule ID: %s\n--name='%s' --filter='%s' --action=%s"\
               % (self.id, self.name, self.filter, self.action)
