import json
import os
from pprint import pprint
from Utils.executeRest import execute
from Utils.incapError import IncapError
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def r_sites(args):
    output = 'Getting site list.'
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "page_size": args.page_size,
        "page_num": args.page_num,
    }

    result = read(param)

    pprint(result)
    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        for site in result['sites']:
            try:
                logger.debug(args.export)
                if args.export:
                    if not os.path.exists(args.path):
                        os.makedirs(args.path)
                    with open(args.path + '/' + site.get('domain')+'.json' or 'none.json', 'w') as outfile:
                        json.dump(site, outfile)
            except OSError as e:
                logger.error(e.strerror)
            if 'acls' in site['security']:
                for aclRules in site['security']['acls']['rules']:
                    logger.debug(aclRules['id'])
                    if aclRules['id'] == 'api.acl.blacklisted_ips':
                        logger.debug('The following IPs are blacklisted: %s' % ', '.join(aclRules['ips']))
                    elif aclRules['id'] == 'api.acl.whitelisted_ips':
                        logger.debug('The following IPs are whitelisted: %s' % ', '.join(aclRules['ips']))
                    else:
                        logger.debug("Nothing is being blacklisted or whitelisted.")
            else:
                logger.debug("No ACLs here...")
            logger.debug(' Domain: %s\n    Status: %s\n    Site ID: %s'
                  % (site.get('domain'), site.get('status'), site.get('site_id')))
        return result.get('res')


def read(params):
    resturl = '/api/prov/v1/sites/list'
    return execute(resturl, params)
