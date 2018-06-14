from Sites.uWhitelist import update
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class IncapException:
    def __init__(self, rule, site_id, rule_id, rule_name):
        self.exceptions = []
        for exceptions in rule:
            except_value = {'site_id': site_id, 'rule_id': rule_id}
            for value in exceptions['values']:
                for k, v in value.items():
                    if type(v) == list and 'urls' in k:
                        urls = list([])
                        url_patterns = list([])
                        for url in v:
                            urls.append(''.join(url['value']))
                            url_patterns.append(''.join(url['pattern']))
                            except_value['urls'] = ','.join(urls)
                            except_value['url_patterns'] = ','.join(url_patterns)
                    elif type(v) == list:
                        except_value[k] = ','.join(v)
                    elif 'geo' in k:
                        if 'countries' in v:
                            except_value['countries'] = ','.join(v['countries'])
                        if 'continents' in v:
                            except_value['continents'] = ','.join(v['continents'])

                logger.info("Add {} exception to {}.".format(value['name'], rule_name))
            self.exceptions.append(except_value)

    def update(self):
        for exception in self.exceptions:
            update(exception)
