from Utils.executeRest import execute
import logging
import json
from Utils.incapError import IncapError
from Accounts.account_audit import Audit


def r_audit(args):
    output = 'Get account audit events.'
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

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
    logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    elif 'audit_events' in result:
        print('Account audit events following:\n')
        for events in result.get('audit_events'):
            audit = Audit(events)
            print(audit.log())


def read(params):
    resturl = '/api/prov/v1/accounts/audit'

    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logging.error('No domain parameter has been passed in.')
    else:
        logging.error('No parameters where passed in.')
