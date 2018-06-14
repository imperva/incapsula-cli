import time
from pprint import pprint
from Utils.executeRest import execute
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def r_audit(args):
    output = 'Get account audit events.'
    logger.debug(output)

    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "account_id": args.account_id,
        "time_range": args.time_range,
        "start": args.start,
        "end": args.end,
        "type": args.type,
        "page_size": args.page_size,
        "page_num": args.page_num
    }

    result = read(param)
    plogger.debug(result)

    if result.get('res') != 0:
        logger.debug('Result Code: %s\nResult Message: %s\nDebug Id-Info: %s' % (
            str(result.get('res')), result.get('res_message'), result.get('debug_info').get('id-info')))
    elif 'audit_events' in result:
        logger.debug('Account audit events following:\n')
        for event in result.get('audit_events'):
            created = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(int(event.get('createdAt'))/1000.0))
            logger.debug('Audit Details:\nTime:%s - Account:%s\nDescription:%s\nContext:%s - '
                  'Changes:%s' % (created, event.get('account_id'),
                                  event.get('type_description'), event.get('context'),
                                  event.get('changes')))


def read(params):
    resturl = '/api/prov/v1/accounts/audit'

    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logger.error('No domain parameter has been passed in.')
    else:
        logger.error('No parameters where passed in.')
