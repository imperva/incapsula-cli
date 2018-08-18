import json
import os
import time
import Sites.rIncapRule
from Config.configuration import IncapConfigurations
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
        return err
    else:
        for site in result['sites']:
            print('FQDN: %s - Status: %s - Site ID: %s'
                  % (site.get('domain'), site.get('status'), site.get('site_id')))
        if args.export:
            config = IncapConfigurations()
            if args.path is None:
                dir_file = config.get_repo()
            else:
                dir_file = args.path
            export_site(result, dir_file, param)
        return result.get('res_message')


def export_site(sites, path, param):
    #print(path)
    file_time = time.strftime("%Y%m%d-%H%M%S")
    #param.pop('tests', None)

    #print(incap_rules['incap_rules'])

    # logging.debug('Incap Rules Response: {}', format(json.dumps(incap_rules, indent=4)))

    # print(result)
    #logging.debug('Incap Rules Response: {}'.format(json.dumps(result, indent=4)))
    del param['account_id']
    for site in sites['sites']:
        try:
            param['site_id'] = site['site_id']
            incap_rules = Sites.rIncapRule.read(param)
            print(incap_rules)
            if incap_rules['res'] == '0':
                incap_rules.pop('res', None)
                del site['incap_rules']
                site['policies'] = incap_rules
            file_name = path + '/' + site.get('domain') + '.json-{}'.format(file_time)
            if not os.path.exists(path):
                os.makedirs(path)
            with open(file_name, 'w') as outfile:
                json.dump(site, outfile)
                print("Exported results to {}...".format(file_name))
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
