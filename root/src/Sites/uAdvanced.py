from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def u_advanced(args):
    output = 'Update advanced cache setting on {0}.'. format(args.site_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "param": args.param,
        "value": args.value
    }
    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        logger.debug('Result Message: %s' % (result.get('res_message')))


def update(params):
    resturl = '/api/prov/v1/sites/performance/advanced'
    if params:
        if "site_id" in params and "param" in params and "value" in params:
            return execute(resturl, params)
        else:
            logger.error('No site ID, parameter or value has been passed in.')
    else:
        logger.error('No parameters where applied.')