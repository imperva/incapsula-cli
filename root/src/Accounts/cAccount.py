from Utils.executeRest import execute
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def c_account(args):
    output = 'With API_ID{0}, API Key={1} lets add {2}!'. format(args.api_id, args.api_key, args.account_name)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "email": args.email,
        "parent_id": args.parent_id,
        "ref_id": args.ref_id,
        "user_name": args.user_name,
        "plan_id": args.plan_id,
        "log_level": args.log_level,
        "logs_account_id": args.logs_account_id,
        "account_name": args.account_name
    }
    result = create(param)

    if result['res'] != 0:
        logger.debug('Result Code: %s\nResult Message: %s\nDebug Id-Info: %s' % (
            str(result['res']), result['res_message'], result['debug_info']['id-info']))


def create(params):
    resturl = '/api/prov/v1/accounts/add'
    if params:
        if "email" in params:
            return execute(resturl, params)
        else:
            logger.debug("Error: No email parameter has been passed in for %s." % __name__)
    else:
        logger.error('No parameters where passed in.')