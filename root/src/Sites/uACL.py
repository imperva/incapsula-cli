from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
import Utils.log
import logging


def u_acl(args):
    output = 'Update ACL rule: {0}'. format(args.rule_id)
    logging.debug(output)

    if args.rule_id == 'blacklisted_countries' and args.countries is None:
        logging.debug("Black listing countries and/or continents requires --countries or --continent option.")
        exit(0)
    if args.rule_id == 'blacklisted_urls' and (args.url_patterns is None and args.urls != ''):
        logging.debug("Black listing urls requires --url_patterns or --urls option.")
        exit(0)

    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "rule_id": 'api.acl.' + args.rule_id,
        "urls": args.urls,
        "url_patterns": args.url_patterns,
        "countries": args.countries,
        "continents": args.continents,
        "ips": args.ips
    }

    update(param)


def update(params):
    resturl = '/api/prov/v1/sites/configure/acl'
    if params:
        if "site_id" in params and "rule_id" in params:
            logging.info('Create a {} ACL rule for site ID:{}'.format(str.replace(params.get('rule_id').replace('_', ' '),
                        'api.acl.', ''), params.get('site_id')))
            result = execute(resturl, params)
            if result.get('res') != 0:
                IncapError(result).log()
            else:
                logging.info('Created a {} ACL rule for site ID:{}'.format(str.replace(params.get('rule_id').replace('_', ' '),
                            'api.acl.', ''), params.get('site_id')))
                return Site(result)
        else:
                logging.error('No site_id or rule_id parameter has been passed in.')
    else:
        logging.error('No parameters where applied.')
