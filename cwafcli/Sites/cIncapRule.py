from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging

from ..Utils.incapResponse import IncapResponse


def c_incaprule(args):
    output = 'Create incapRule = {0} for site: {1}'. format(args.name, args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
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

    result = create(param)
    if result.get('res') != '0':
        err = IncapError(result)
        err.log()
    else:
        resp = IncapResponse(result)
        print('Created IncapRule ID: {}'.format(resp.get_rule_id()))
        resp.log()
        return resp


def create(params):
    resturl = 'sites/incapRules/add'
    if params:
        if "site_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
