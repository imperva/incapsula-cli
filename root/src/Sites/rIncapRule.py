from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def r_incaprule(args):
    output = 'Get incapRules for site: {0}'. format(args.site_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "include_ad_rules": args.include_ad_rules,
        "include_incap_rules": args.include_incap_rules,
        "page_size": args.page_size,
        "page_num": args.page_num

    }

    read(param)


def read(params):
    resturl = '/api/prov/v1/sites/incapRules/list'
    if params:
        if "site_id" in params:
            logger.info('Get IncapRule(s) for site ID:{}'.format(params.get('site_id')))
            result = execute(resturl, params)
            print(result)
            if result.get('res') != '0':
                IncapError(result).log()
            else:
                if 'incap_rules' in result:
                    if 'All' in result['incap_rules']:
                        for rule in result['incap_rules']['All']:
                            logger.debug('IncapRule ID={id} -- Name={name} -- Enable={enabled} -- Filter={filter}'
                                         .format(**rule))
                    if 'ad_rules_data' in result['incap_rules']:
                        if 'Redirect' in result['incap_rules']['ad_rules_data']:
                            for rule in result['incap_rules']['ad_rules_data']['Redirect']:
                                logger.debug('Redirect ID={id} -- Name={name} -- Enable={enabled}'
                                             ' -- Priority={priority} -- response_code={response_code}'
                                             ' from={from} -> to:{to} -- Filter={filter}'.format(**rule))
                        if 'Forward' in result['incap_rules']['ad_rules_data']:
                            for rule in result['incap_rules']['ad_rules_data']['Forward']:
                                logger.debug('Forward ID={id} -- Name={name} -- Enable={enabled}'
                                             ' -- Priority={priority} -- response_code={response_code}'
                                             ' from={from} -> to:{to} -- Filter={filter}'.format(**rule))
                        if 'Rewrite' in result['incap_rules']['ad_rules_data']:
                            for rule in result['incap_rules']['ad_rules_data']['Rewrite']:
                                logger.debug('Rewrite ID={id} -- Name={name} -- Enable={enabled}'
                                             ' -- Priority={priority} -- response_code={response_code}'
                                             ' from={from} -> to:{to} -- Filter={filter}'.format(**rule))
                    else:
                        logger.info('You have no IncapRules!!!')
            return result
        else:
            logger.error('No site ID parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
