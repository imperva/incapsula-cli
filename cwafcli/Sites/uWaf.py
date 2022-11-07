from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging


def u_security(args):
    param = vars(args)
    #action = param['do']
    output = 'Update site {0} security configuration.'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))

    if args.rule_id == 'ddos' and args.activation_mode == '':
        logging.warning('Activation mode param is required:\n'
                     'activation_mode=api.threats.ddos.activation_mode.auto\n'
                     'activation_mode=api.threats.ddos.activation_mode.off\n'
                     'activation_mode=api.threats.ddos.activation_mode.on')
        exit(0)

    activation_mode = ''
    rule_id = ''
    security_rule_action = ''

    if args.activation_mode:
        activation_mode = 'api.threats.ddos.activation_mode.' + args.activation_mode
    if args.rule_id:
        rule_id = 'api.threats.' + args.rule_id
    if args.security_rule_action:
        security_rule_action = 'api.threats.action.' + args.security_rule_action

    param['rule_id'] = rule_id
    param['activation_mode'] = activation_mode
    param['security_rule_action'] = security_rule_action
    # param = {"api_id": args.api_id,
    #     "api_key": args.api_key,
    #     "site_id": args.site_id,
    #     "rule_id": rule_id,
    #     "block_bad_bots": args.block_bad_bots,
    #     "challenge_suspected_bots": args.challenge_suspected_bots,
    #     "activation_mode": activation_mode,
    #     "security_rule_action": security_rule_action,
    #     "quarantined_urls": args.quarantined_urls,
    #     "ddos_traffic_threshold": args.ddos_traffic_threshold
    # }

    result = update(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        return err
        # err.log()
    else:
        # site = Site(result)
        # print('Updated {} Security(WAF) Rule for {}.'.format(args.rule_id.replace('_', ' '), site.domain))
        return result


def update(params):
    resturl = 'sites/configure/security'
    if params:
        if "site_id" in params and "rule_id" in params:
            result = execute(resturl, params)
            return result
        else:
            logging.warning("No site_id or rule_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')