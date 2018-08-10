from Utils.executeRest import execute
from Sites.adr_incaprule import IncapRule
from Sites.adr_incaprule import ADRuleRewrite
from Sites.adr_incaprule import ADRuleRedirect
from Sites.adr_incaprule import ADRuleForward
from Utils.incapError import IncapError
import logging
import json


def r_incaprule(args):
    output = 'Get incapRules for site: {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "include_ad_rules": args.include_ad_rules,
        "include_incap_rules": args.include_incap_rules,
        "page_size": args.page_size,
        "page_num": args.page_num

    }

    result = read(param)
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != "0":
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
                    adr_rule = ADRuleRewrite(rule)
                    print(adr_rule.log())
            else:
                logging.info('You have no Rewrite Rules!!!')
    return result


def read(params):
    resturl = '/api/prov/v1/sites/incapRules/list'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
