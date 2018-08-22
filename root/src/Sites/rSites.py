import json
import os
import time
import Sites.rIncapRule
from Config.configuration import IncapConfigurations
from Sites.site import Site
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
                path = config.get_repo()
            else:
                path = args.path
            filename = args.filename
            export_site(result, path, filename, param)
        return result.get('res_message')


def export_site(sites, path, filename, param):
    file_time = time.strftime("%Y%m%d-%H%M%S")
    del param['account_id']
    for site in sites['sites']:
        try:
            if 'incap_rules' in site:
                print(len(site['incap_rules']))
                del site['incap_rules']
            param['site_id'] = site['site_id']
            incap_rules = Sites.rIncapRule.read(param)
            print(len(incap_rules))
            if incap_rules['res'] == '0':
                incap_rules.pop('res', None)
                site['policies'] = incap_rules
            #file_name = path + '/' + site.get('domain') + '.json-{}'.format(file_time)
            _filename = path + '/' + create_filename(filename, site) + '.json'
            print("Export file name: {}". format(_filename))
            if not os.path.exists(path):
                os.makedirs(path)
            with open(_filename, 'w') as outfile:
                json.dump(site, outfile, indent=4)
                print("Exported results to {}...".format(_filename))
        except OSError as e:
            logging.error(e.strerror)


def create_filename(filename, site):
    site = Site(site)
    if filename == "{site_id}_{domain}":
        return "{}_{}".format(site.domain, site.site_id)
    elif filename == "{domain}":
        return "{}".format(site.domain)
    elif filename == "{site_id}":
        return "{}".format(site.site_id)
    elif filename.startswith("{site_id}_{domain}") and not filename.endswith("_{date}"):
        return "{}_{}_{}".format(site.site_id, site.domain,
                                 filename.replace("{site_id}_{domain}", '').replace('.', '_'))
    else:
        return "{}_{}_{}".format(site.site_id, site.domain, time.strftime("%Y%m%d-%H%M%S"))


def read(params):
    resturl = '/api/prov/v1/sites/list'
    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No account_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
