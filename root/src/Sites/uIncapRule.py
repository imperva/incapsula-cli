from Sites.site import Site
from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError
logger = Utils.log.setup_custom_logger(__name__)


def u_incaprule(args):
    output = 'Update incapRule Id: {}'. format(args.rule_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "rule_id": args.rule_id,
        "name": args.name,
        "action": args.action,
        "filter": args.filter,
        "response_code": args.response_code,
        "protocol": args.protocol,
        "add_missing": args.add_missing,
        "from": args.origin,
        "to": args.to,
        "rewrite_name": args.rewrite_name,
        "dc_id": args.dc_id,
        "is_test_mode": args.is_test_mode,
        "lb_algorithm": args.lb_algorithm
    }

    update(param)


def update(params):
    resturl = '/api/prov/v1/sites/incapRules/edit'
    if params:
        if "rule_id" in params:
            logger.info('Update IncapRule for ID:{}'.format(params.get('rule_id')))
            result = execute(resturl, params)
            if result.get('res') != '0':
                IncapError(result).log()
            else:
                logger.info('Updated the following incapRule Id: {}"'.format(result.get('rule_id')))
                return result
        else:
            logger.error('No rule ID parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
