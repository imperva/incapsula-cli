import logging


class IncapExceptions:
    def __init__(self, rule, site_id, rule_id, rule_name):
        logging.debug('IncapExceptions: {}'.format(rule))
        for exceptions in rule:
            param = {
                "api_id": None,
                "api_key": None,
                "site_id": site_id,
                "rule_id": rule_id,
                "urls": '',
                "countries": '',
                "continents": '',
                "ips": '',
                "whitelist_id": '',
                "delete_whitelist": '',
                "client_app_types": '',
                "client_apps": '',
                "parameters": '',
                "user_agents": ''
            }
            for value in exceptions['values']:
                for k, v in value.items():
                    logging.debug('Exception key={}:value={}'.format(k, v))
                    if 'urls' in k:
                        urls = list([])
                        for url in v:
                            urls.append(''.join(url['value']))
                            param['urls'] = ','.join(urls)
                            print(' Add {} exception(s) to {}: "{}"'
                                  .format(value['name'], rule_name.lower(), param['urls']))
                    elif 'geo' in k:
                        if 'countries' in v:
                            param['countries'] = ','.join(v['countries'])
                            print(' Add {} exception(s) to {}: "{}"'
                                  .format(value['name'], rule_name.lower(), param['countries']))
                        if 'continents' in v:
                            param['continents'] = ','.join(v['continents'])
                            print(' Add {} exception(s) to {}: "{}"'
                                  .format(value['name'], rule_name.lower(), param['continents']))
                    elif 'client_app_types' in k:
                        param['client_app_types'] = ','.join(v)
                        print(' Add {} exception(s) to {}: "{}"'
                              .format(value['name'], rule_name.lower(), param['client_app_types']))
                    elif 'client_apps' in k:
                        param['client_apps'] = ','.join(v)
                        print(' Add {} exception(s) to {}: "{}"'
                              .format(value['name'], rule_name.lower(), param['client_apps']))
                    elif 'ips' in k:
                        param['ips'] = ','.join(v)
                        print(' Add {} exception(s) to {}: "{}"'
                              .format(value['name'], rule_name.lower(), param['ips']))
                    elif 'parameters' in k:
                        param['parameters'] = ','.join(v)
                        print(' Add {} exception(s) to {}: "{}"'
                              .format(value['name'], rule_name.lower(), param['parameters']))
                    elif 'user_agents' in k:
                        param['user_agents'] = ','.join(v)
                        print(' Add {} exception(s) to {}: "{}"'
                              .format(value['name'], rule_name.lower(), param['user_agents']))
            logging.debug('Exception Params: {}'.format(param))
            from ..Sites.uWhitelist import update
            update(param)


class IncapException:
    def __init__(self, rule):
        logging.debug('IncapException: {}'.format(rule))
        self.id = rule['id']
        self.urls = None
        self.countries = None
        self.continents = None
        self.ips = None
        self.whitelist_id = None
        self.client_app_types = None
        self.client_apps = None
        self.parameters = None
        self.user_agents = None

        for k, v in rule.items():
            logging.debug('Exception key={}:value={}'.format(k, v))
            if 'urls' in k:
                urls = list([])
                for url in v:
                    urls.append(''.join(url['value']))
                    self.urls = ','.join(urls)
            elif 'geo' in k:
                if 'countries' in v:
                    self.countries = ','.join(v['countries'])
                if 'continents' in v:
                    self.continents = ','.join(v['continents'])
            elif 'client_app_types' in k:
                self.client_app_types = ','.join(v)
            elif 'client_apps' in k:
                self.client_apps = ','.join(v)
            elif 'ips' in k:
                self.ips = ','.join(v)
            elif 'parameters' in k:
                self.parameters = ','.join(v)
            elif 'user_agents' in k:
                self.user_agents = ','.join(v)


