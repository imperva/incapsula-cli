from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging

from ..Utils.incapResponse import IncapResponse


def u_incaprule(args):
    output = 'Update incapRule Id: {}'. format(args.rule_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
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

    result = update(param)
    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        resp = IncapResponse(result)
        print('Updated IncapRule ID: {}'.format(param.get('rule_id')))
        resp.log()
        return resp


def update(params):
    resturl = 'sites/incapRules/edit'
    if params:
        if "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
