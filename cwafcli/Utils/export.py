import json
import os
import time

from ..Sites.dataCenters import DataCenter
from ..Sites.incapRules import IncapRule
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging


def export(args):
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))

    if args.site_id is None:
        page = 0
        end_page = 0
        param = vars(args)
        param['page_size'] = 100
        param['site_id'] = ''

        while True:
            param['page_num'] = page
            from ..Sites.rSites import read
            result = read(param)

            if int(result.get('res')) != 0:
                err = IncapError(result)
                err.log()
                return err
            elif result['sites']:
                start_page = (end_page + 1)
                end_page += len(result['sites'])
                logging.debug("Exporting pages from {} to {}".format(start_page, end_page))
                for site in result['sites']:
                    if args.path is None:
                        from ..Config.configuration import IncapConfigurations
                        path = os.getenv("IMPV_REPO", IncapConfigurations.get_config(param["profile"], 'repo'))
                        if not path:
                            logging.warning('No path was provided.')
                            exit(0)
                    else:
                        path = args.path
                    filename = args.filename
                    export_site(site, path, filename, args)
                page += 1
            else:
                break
    else:
        result = Site.read(args)
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
            return err
        else:
            if args.path is None:
                from ..Config.configuration import IncapConfigurations
                path = os.getenv("IMPV_REPO", IncapConfigurations.get_config(args.profile, 'repo'))
                if not path:
                    logging.warning('No path was provided.')
                    exit(0)
            else:
                path = args.path
            filename = args.filename
            export_site(result, path, filename, args)


def export_site(site, path, filename, args):
    try:
        if 'incap_rules' in site:
            del site['incap_rules']
        args.site_id = site['site_id']
        args.do = 'list'
        incap_rules = IncapRule.commit(args)
        if incap_rules['res'] == '0':
            incap_rules.pop('res', None)
            site['policies'] = incap_rules
        data_centers = DataCenter.commit(args)
        if data_centers['res'] == '0':
            data_centers.pop('res', None)
            site['dataCenters'] = data_centers
        _filename = path + '/' + create_filename(filename, site) + '.json'
        logging.debug("Export file name: {}". format(_filename))
        if not os.path.exists(path):
            os.makedirs(path)
        with open(_filename, 'w') as outfile:
            json.dump(site, outfile, indent=4)
            logging.debug("Exported results to {}...".format(_filename))
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

