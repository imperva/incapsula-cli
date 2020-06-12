from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging


def u_whitelist(args):
    param = vars(args)
    #action = param['do']
    output = 'Update whitelist rule ID={0}.'. format(args.rule_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)

    rule_id = ''
    if "listed" in args.rule_id:
        param['rule_id'] = 'api.acl.' + args.rule_id
    else:
        param['rule_id'] = 'api.threats.' + args.rule_id

    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        site = Site(result)
        print('Updated successful')
        return site


def update(params):
    resturl = 'sites/configure/whitelists'
    if params:
        if "site_id" in params and "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No site_id or rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')
