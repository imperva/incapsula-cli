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

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        for site in result['sites']:
            print('FQDN: %s - Status: %s - Site ID: %s'
                  % (site.get('domain'), site.get('status'), site.get('site_id')))
        if args.export:
            export(result, args.path)
        return result.get('res')


def export(sites, path):
    for site in sites['sites']:
        try:
            print("Exporting results...")
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + '/' + site.get('domain') + '.json' or 'none.json', 'w') as outfile:
                json.dump(site, outfile)
        except OSError as e:
            logging.error(e.strerror)


def read(params):
    resturl = '/api/prov/v1/sites/list'
    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No account_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
