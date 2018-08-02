from Utils.executeRest import execute
from Sites.site import Site
from Utils.incapError import IncapError
import Utils.log
import logging


def u_security(args):
    output = 'Update site {0} security configuration.'. format(args.site_id)
    logging.debug(output)

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

    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "rule_id": rule_id,
        "block_bad_bots": args.block_bad_bots,
        "challenge_suspected_bots": args.challenge_suspected_bots,
        "activation_mode": activation_mode,
        "security_rule_action": security_rule_action,
        "quarantined_urls": args.quarantined_urls,
        "ddos_traffic_threshold": args.ddos_traffic_threshold
    }

    update(param)


def update(params):
    resturl = '/api/prov/v1/sites/configure/security'
    if params:
        if "site_id" in params and "rule_id" in params:
            logging.info('Create a {} rule for site ID:{}'.format(str.replace(params.get('rule_id').replace('_', ' '),
                        'api.threats.', ''), params.get('site_id')))
            result = execute(resturl, params)
            if result.get('res') != 0:
                IncapError(result).log()
            else:
                logging.info('Created a {} rule for site ID:{}'.format(str.replace(params.get('rule_id').replace('_', ' '),
                            'api.threats.', ''), params.get('site_id')))
                return Site(result)
        else:
                logging.error('No domain parameter has been passed in.')
    else:
        logging.error('No parameters where applied.')