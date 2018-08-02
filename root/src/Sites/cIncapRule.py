from Utils.executeRest import execute
from Utils.incapError import IncapError
import Utils.log
import logging


def c_incaprule(args):
    output = 'Create incapRule = {0} for site: {1}'. format(args.name, args.site_id)
    logging.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
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

    create(param)


def create(params):
    resturl = '/api/prov/v1/sites/incapRules/add'
    if params:
        if "site_id" in params:
            logging.info('Create IncapRule for site ID:{}'.format(params.get('site_id')))
            result = execute(resturl, params)
            if result.get('res') != '0':
                IncapError(result).log()
            else:
                logging.info('Created the following incapRule Id: {}'.format(result.get('rule_id')))
                return result
        else:
            logging.error('No site ID parameter has been passed in.')
    else:
        logging.error('No parameters where passed in.')
