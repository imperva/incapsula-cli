import json
import os
from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging


def r_sites(args):
    output = 'Getting site list.'
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "page_size": args.page_size,
        "page_num": args.page_num,
    }

    result = read(param)
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        for site in result['sites']:
            try:
                logging.debug("Export results: {}.".format(args.export))
                if args.export:
                    if not os.path.exists(args.path):
                        os.makedirs(args.path)
                    with open(args.path + '/' + site.get('domain')+'.json' or 'none.json', 'w') as outfile:
                        json.dump(site, outfile)
            except OSError as e:
                logging.error(e.strerror)
            # if 'acls' in site['security']:
            #     for aclRules in site['security']['acls']['rules']:
            #         logging.debug(aclRules['id'])
            #         if aclRules['id'] == 'api.acl.blacklisted_ips':
            #             logging.info('The following IPs are blacklisted: %s' % ', '.join(aclRules['ips']))
            #         elif aclRules['id'] == 'api.acl.whitelisted_ips':
            #             logging.info('The following IPs are whitelisted: %s' % ', '.join(aclRules['ips']))
            #         else:
            #             logging.info("Nothing is being blacklisted or whitelisted.")
            # else:
            #     logging.debug("No ACLs here...")
            print('FQDN: %s - Status: %s - Site ID: %s'
                  % (site.get('domain'), site.get('status'), site.get('site_id')))
        return result.get('res')


def read(params):
    resturl = '/api/prov/v1/sites/list'

    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logging.error('No account_id parameter has been passed in.')
    else:
        logging.error('No parameters where passed in.')
