from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.incapResponse import IncapResponse


def d_incaprule(args):
    output = 'Delete incapRule ID = {0}'. format(args.rule_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "rule_id": args.rule_id
    }

    result = delete(param)

    if result.get('res') != '0':
        err = IncapError(result)
        err.log()
    else:
        print('Deleted IncapRule ID:{}'.format(param.get('rule_id')))
        resp = IncapResponse(result)
        resp.log()
        return resp


def delete(params):
    resturl = 'sites/incapRules/delete'
    if params:
        if "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
