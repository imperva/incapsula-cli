from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def c_site(args):
    output = 'Creating site = {0}'. format(args.domain)
    logger.debug(output)
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

    return create(param)


def create(params):
    resturl = '/api/prov/v1/sites/add'
    if params:
        if "domain" in params:
            result = execute(resturl, params)
            if result.get('res') != 0:
                err = IncapError(result)
                err.log()
            else:
                site = Site(result)
                site.log()
                #return site
            return result
        else:
            logger.error('No domain parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
