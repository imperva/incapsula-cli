import json
from Utils.SiteEncoder import SiteEncoder
from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def r_site(args):
    output = 'Get site status for ID = {0}'. format(args.site_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "tests": args.tests,
        "site_id": args.site_id
    }
    result = read(param)
    from pprint import pprint
    pprint(result)
    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        site = Site(result)
        site.log()
        return site


def read(params):
    resturl = '/api/prov/v1/sites/status'

    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logger.error('No domain parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
