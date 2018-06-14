from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def d_incaprule(args):
    output = 'Delete incapRule ID = {0}'. format(args.rule_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "rule_id": args.rule_id
    }

    delete(param)


def delete(params):
    resturl = '/api/prov/v1/sites/incapRules/delete'
    if params:
        if "rule_id" in params:
            logger.info('Delete IncapRule ID:{}'.format(params.get('rule_id')))
            result = execute(resturl, params)
            if result.get('res') != '0':
                IncapError(result).log()
            else:
                logger.info('Deleted the following incapRule Id: {}"'.format(params.get('rule_id')))
                return result
        else:
            logger.error('No rule ID parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
