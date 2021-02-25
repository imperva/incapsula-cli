from ..Sites.cIncapRule import create
from ..Utils.executeRest import execute
import logging

from ..Utils.incapError import IncapError


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
        self.to = data.get('to') or ""
        self.id = data['id']
        self.enabled = data['enabled']
        self.priority = data['priority']
        self.add_missing = str(data.get('add_missing'))
        self.last_7_days_requests_count = data['last_7_days_requests_count']
        self.name = data['name']
        self.action = data['action']
        self._from = data.get('from') or ""
        self.filter = data['filter']
        self.allow_caching = str(data.get('allow_caching'))
        self.rewrite_name = data.get('rewrite_name') or ""

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Rule ID: %s -- Rule Name: %s\n' \
               '--to="%s" --from="%s" --name="%s" --rewrite_name="%s" --allow_caching=%s' \
               ' --add_missing=%s --filter="%s" --action=%s'\
               % (self.id, self.name, self.to, self._from, self.name, self.rewrite_name,
                  self.allow_caching, self.add_missing, self.filter, self.action)


class ADRuleRewriteResponse:
    def __init__(self, data):
        self.to = data.get('to') or ""
        self.id = data['id']
        self.enabled = data['enabled']
        self.add_missing = str(data.get('add_missing'))
        self.last_7_days_requests_count = data['last_7_days_requests_count']
        self.name = data['name']
        self.action = data['action']
        self._from = data.get('from') or ""
        self.filter = data['filter']
        self.allow_caching = str(data.get('allow_caching'))
        self.rewrite_name = data.get('rewrite_name') or ""

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
        self.dc_id = data.get('dc_id') or ""
        self.filter = data['filter']
        self.allow_caching = str(data.get('allow_caching'))
        self.port_forwarding_value = data.get("port_forwarding_value") or ""
        self.port_forwarding_context = data.get("port_forwarding_context") or ""

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Rule ID: %s -- Rule Name: %s\n' \
               '--name="%s" --dc_id="%s"' \
               ' --allow_caching=%s --filter="%s" --action=%s --port_forwarding_value=%s --port_forwarding_context=%s'\
               % (self.id, self.name, self.name, self.dc_id,
                  self.allow_caching, self.filter, self.action, self.port_forwarding_value, self.port_forwarding_context)


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

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        print('{} IncapRule.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'sites/incapRules/{}'.format(param['do'])

        if action == 'list':
            result = execute(resturl, param)
            IncapRule._list(result)
            return result
        elif action == "get":
            resturl2 = "/sites/{site_id}/rules/{rule_id}".format(**param)
            result = execute(resturl2, param, "GET")
            url = "/sites/{site_id}/rules".format(**param)
            execute(url, param, 'POST', result)
        else:
            result = execute(resturl, param)
            IncapRule._execute(result, action)
            print("IncapRule Result: {}".format(result))
            return result

    @staticmethod
    def _execute(result, action):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
            return err
        else:
            print('{} successful on IncapRule {}'
                  .format(action[0].upper() + action[1:], result.get('rule_id') or ''))

    @staticmethod
    def _list(result):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
        else:
            if 'incap_rules' in result:
                if 'All' in result['incap_rules']:
                    for rule in result['incap_rules']['All']:
                        incap_rule = IncapRule(rule)
                        print(incap_rule.log())
                else:
                    logging.info('You have no IncapRules!!!')

            if 'custom_error_response_rules' in result:
                if 'RewriteResponse' in result['custom_error_response_rules']:
                    for rule in result['custom_error_response_rules']['RewriteResponse']:
                        incap_rule = IncapRule(rule)
                        print(incap_rule.log())
                else:
                    logging.info('You have no IncapRules!!!')

            if 'delivery_rules' in result:
                if 'Redirect' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Redirect']:
                        adr_rule = ADRuleRedirect(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Redirect Rules!!!')

                if 'Forward' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Forward']:
                        adr_rule = ADRuleForward(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Forward Rules!!!')

                if 'Rewrite' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Rewrite']:
                        data = ""
                        for k, v in rule.items():
                            if k == "filter" and v == "":
                                data += 'URL contains "^/"'
                            elif k == "filter" and v != "":
                                data += "--{}='{}' ".format(k, v)
                            else:
                                data += '--{}="{}" '. format(k, v)
                        print("RULE: {}".format(rule))
                        adr_rule = ADRuleRewrite(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Rewrite Rules!!!')
                if 'RewriteResponse' in result['delivery_rules']:
                    for rule in result['delivery_rules']['RewriteResponse']:
                        data = ""
                        for k, v in rule.items():
                            if k == "filter" and v == "":
                                data += 'URL contains "^/"'
                            elif k == "filter" and v != "":
                                data += "--{}='{}' ".format(k, v)
                            else:
                                data += '--{}="{}" '. format(k, v)
                        print("RULE: {}".format(rule))
                        adr_rule = ADRuleRewriteResponse(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no RewriteResponse Rules!!!')

    @staticmethod
    def _copy(result, ):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
        else:
            if 'incap_rules' in result:
                if 'All' in result['incap_rules']:
                    for rule in result['incap_rules']['All']:
                        incap_rule = IncapRule(rule)
                        print(incap_rule.log())
                else:
                    logging.info('You have no IncapRules!!!')

            if 'delivery_rules' in result:
                if 'Redirect' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Redirect']:
                        adr_rule = ADRuleRedirect(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Redirect Rules!!!')

                if 'Forward' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Forward']:
                        adr_rule = ADRuleForward(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Forward Rules!!!')

                if 'Rewrite' in result['delivery_rules']:
                    for rule in result['delivery_rules']['Rewrite']:
                        data = ""
                        del rule["id"]
                        del rule["enabled"]
                        del rule["priority"]
                        del rule["allow_caching"]
                        del rule["last_7_days_requests_count"]

                        for k, v in rule.items():
                            if k == "filter" and v == "":
                                data += 'URL contains "^/"'
                            elif k == "filter" and v != "":
                                data += "--{}='{}' ".format(k, v)
                            else:
                                data += '--{}="{}" '. format(k, v)

                        adr_rule = ADRuleRewrite(rule)
                        print(adr_rule.log())
                else:
                    logging.info('You have no Rewrite Rules!!!')