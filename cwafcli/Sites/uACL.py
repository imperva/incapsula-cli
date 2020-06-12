from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging


def u_acl(args):
    param = vars(args)
    #action = param['do']
    output = 'Update ACL rule: {0}'. format(args.rule_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    if args.rule_id == 'blacklisted_countries' and args.countries is None:
        logging.warning("Black listing countries and/or continents requires --countries or --continent option.")
        exit(0)
    if args.rule_id == 'blacklisted_urls' and (args.url_patterns is None and args.urls != ''):
        logging.warning("Black listing urls requires --url_patterns or --urls option.")
        exit(0)

    param['rule_id'] = 'api.acl.' + args.rule_id

    # param = {
    #     "api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "site_id": args.site_id,
    #     "rule_id": 'api.acl.' + args.rule_id,
    #     "urls": args.urls,
    #     "url_patterns": args.url_patterns,
    #     "countries": args.countries,
    #     "continents": args.continents,
    #     "ips": args.ips
    # }

    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
    else:
        site = Site(result)
        print('Updated {} ACL Rule for {}.'.format(args.rule_id.replace('_', ' '), site.domain))
        return site


def update(params):
    resturl = 'sites/configure/acl'
    if params:
        if "site_id" in params and "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No site_id or rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')
