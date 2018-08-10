from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
from Sites.exception import IncapException
import logging


def u_whitelist(args):
    output = 'Update whitelist rule ID={0}.'. format(args.rule_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "rule_id": args.rule_id,
        "urls": args.urls,
        "countries": args.countries,
        "continents": args.continents,
        "ips": args.ips,
        "whitelist_id": args.whitelist_id,
        "delete_whitelist": args.delete_whitelist,
        "client_app_types": args.client_app_types,
        "client_apps": args.client_apps,
        "parameters": args.parameters,
        "user_agents": args.user_agents
    }

    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        site = Site(result)
        for rule in site.waf_rules:
            if rule['id'] == args.rule_id:
                logging.debug('WAF Rules: {}'.format(site.get_waf_rules()))
                print('WAF Rule Name: {} has the following exceptions:'.format(rule['name']))
                for exceptions in rule['exceptions']:
                    logging.debug('Exception ID: {}'.format(exceptions['id']))
                    for exception in exceptions['values']:
                        value = IncapException(exception)
                        print("Exception Type: {}".format(value.id.replace('api.rule_exception_type.', '').replace('_', ' ')))
                #logging.debug('WAF Rules: {}'.format(site.get_waf_rules()))
        print('Updated successful')
        return site


def update(params):
    resturl = '/api/prov/v1/sites/configure/whitelists'
    if params:
        if "site_id" in params and "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No site_id or rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')
