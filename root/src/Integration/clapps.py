from Utils.executeRest import execute
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def r_clapps():
    output = 'Retrieving client apps list for client_app_id to Client Application Name.'
    logger.debug(output)
    param = {
        "api_id": None,
        "api_key": None
    }

    result = read(param)

    if result['res'] != 0:
        logger.debug('Result Code: %s\nResult Message: %s\nDebug Id-Info: %s' % (
            str(result['res']), result['res_message'], result['debug_info']['id-info']))
    else:
        return result


def read(param):
    resturl = '/api/integration/v1/clapps'
    return execute(resturl, param)

