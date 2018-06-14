from Utils.executeRest import execute
from Utils.incapError import IncapError
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def u_configuration(args):
    output = 'Update site {0} with configuration param={1} and value={2}.'. format(args.site_id, args.param, args.value)
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
        logger.debug('Result Code: %s\nResult Message: %s\nDebug Id-Info: %s' % (
            str(result.get('res')), result.get('res_message'), result.get('debug_info').get('id-info')))

    return result.get('res')


def update(params):
    resturl = '/api/prov/v1/sites/configure'
    if params:
        if "param" in params and "value" in params:
            return execute(resturl, params)
        else:
            logger.error('No domain parameter has been passed in.')
    else:
        logger.error('No parameters where applied.')