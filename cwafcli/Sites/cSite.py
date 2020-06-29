from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import json
import logging


def c_site(args):
    output = 'Creating site: {0}'. format(args.domain)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "force_ssl": args.force_ssl,
        "ref_id": args.ref_id,
        "send_site_setup_emails": args.send_site_setup_emails,
        "site_ip": args.site_ip,
        "log_level": args.log_level,
        "logs_account_id": args.logs_account_id,
        "domain": args.domain
    }

    result = create(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        site = Site(result)
        print('Created: %s, ID: %s ' % (site.get_domain(), str(site.get_id())))
        return site


def create(params):
    resturl = 'sites/add'
    if params:
        if "domain" in params:
            return execute(resturl, params)
        else:
            logging.warning("No domain parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
