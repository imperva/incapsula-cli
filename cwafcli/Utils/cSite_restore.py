import json
import os
from ..Sites.incapRules import IncapRule
from ..Sites.site import Site
from ..Sites.cSite import create
from ..Utils.incapError import IncapError
from ..Sites.acl import ACL
from ..Sites.waf import Security

import logging


def c_site_restore(args):
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "domain": args.domain
    }
    from ..Config.configuration import IncapConfigurations
    config = IncapConfigurations()

    if args.path == '':
        dir_file = os.getenv("IMPV_REPO", IncapConfigurations.get_config(args.profile, 'repo'))
    else:
        dir_file = args.path

    try:
        if os.path.isfile(dir_file):
            with open(dir_file, 'r') as file:
                recover_site(file, param)
        else:
            for files in os.listdir(dir_file):
                with open(files, 'r') as file:
                    recover_site(file, param)
    except OSError as e:
        logging.error(e.strerror)
        exit(e.errno)


def recover_site(file, params):
    old_site = Site(json.load(file))
    if params['domain'] is None:
        print('Restoring {0}'. format(old_site.domain))
        params['domain'] = old_site.domain
    else:
        print('Creating {0} from {1} template'.format(params['domain'], old_site.domain))
        result = create(params)
        if int(result.get('res')) != 0:
            logging.error('%s was not created, please review logs.' % params['domain'])
            err = IncapError(result)
            err.log()
        else:
            new_site = Site(result) or None
            print('Created: %s, ID: %s ' % (new_site.get_domain(), str(new_site.get_id())))
            acl = ACL(old_site.security, new_site.site_id)
            acl.update()
            sec = Security(old_site.security, new_site.site_id)
            sec.update()
            if old_site.incap_rules is not []:
                for rule in old_site.incap_rules:
                    logging.debug('Incap Rule JSON Response: {}'.format(json.dumps(rule, indent=4)))
                    incap_rule = IncapRule(rule)
                    incap_rule_params = incap_rule.set_param(new_site.site_id)
                    incap_rule.create_incap_rule(incap_rule_params)

