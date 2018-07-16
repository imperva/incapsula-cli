import json
import os
from Sites.incaprule import IncapRule
from Sites.site import Site
from Sites.cSite import create
import Utils.log
from Utils.incapError import IncapError
from Sites.acl import ACL
from Sites.waf import Security

logger = Utils.log.setup_custom_logger(__name__)


def c_site_restore(args):
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "domain": args.domain
    }
    output = 'Creating bulk sites from {0}'. format(args.path)
    logger.debug(output)

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
        logger.error(e.strerror)
        exit(e.errno)


def recover_site(file, param):
    old_site = Site(json.load(file))
    # param['domain'] = old_site.domain
    # new_site = Site(create(param)) or None
    # if new_site.site_id is None:
    #     logger.warning('%s was not created, please review logs.' % old_site.domain)
    #     exit(1)
    # logger.debug('Created %s, Site_ID=%s, Status=%s' % (new_site.domain, new_site.site_id, new_site.status))

    # acl = ACL(old_site.security, new_site.site_id)
    # acl.update()
    # sec = Security(old_site.security, new_site.site_id)
    # sec.update()
    incaprule = IncapRule(old_site.incap_rules)
    print('here is my incap rule {}'.format(incaprule.name))
    exit(0)


def set_incapRules(data, site_id):
    from Sites.cIncapRule import create
    for incapRule in data:
        print('--------------------------------------------------------------------------------------------')
        name = incapRule['name']
        logger.info("Add %s InacapRule." % name)
        del incapRule['creation_date']
        del incapRule['id']
        incapRule['filter'] = incapRule['rule']
        del incapRule['rule']
        incapRule['site_id'] = site_id
        incapRule['action'] = str.upper(incapRule.get('action').replace('api.rule_action_type.', ''))
        from pprint import pprint
        #pprint(incapRule)
        result = create(incapRule)
        #pprint(result)
        if result['res'] == '0':
            logger.info("Successfully added %s!" % name)
        else:
            logger.error('Failed to add %s - %s' % (name, incapRule))
            err = IncapError(result)
            err.log()
