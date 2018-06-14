from Utils.executeRest import execute
from Utils.incapError import IncapError
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def d_site(args):
    output = 'Delete site ID = {0}!'. format(args.site_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id
    }
    result = delete(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        logger.debug('Result Code: %s\nResult Message: %s\nDebug Id-Info: %s'
              % (str(result.get('res')), result.get('res_message'),
                 result.get('debug_info').get('id-info')))
        return result.get('res')


def delete(params):
    resturl = '/api/prov/v1/sites/delete'

    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logger.error('No domain parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
