from Utils.executeRest import execute
from Sites.site import Site
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def u_whitelist(args):
    output = 'Update whitelist rule ID={0} with whitelist ID={1}.'. format(args.rule_id, args.whitelist_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "rule_id": args.rule_id,
        "urls": args.urls,
        "countries": args.countries,
        "continents": args.continents,
        "ips": args.ips,
        "whitelist_id": args.whitelist_id,
        "delete_whitelist": args.delete_whitelist,
        "client_app_types": args.client_app_types,
        "client_apps": args.client_apps,
        "parameters": args.parameters,
        "user_agents": args.user_agents
    }
    update(param)


def update(params):
    resturl = '/api/prov/v1/sites/configure/whitelists'
    if params:
        if "site_id" in params and "rule_id" in params:
            logger.info('Create a {} exception rule for site ID:{}'.format(str.replace(params.get('rule_id')
                        .replace('_', ' '), 'api.threats.', ''), params.get('site_id')))
            result = execute(resturl, params)
            if result.get('res') != 0:
                IncapError(result).log()
            else:
                logger.info('Created a {} exception rule for site ID:{}'.format(str.replace(params.get('rule_id').replace('_',
                            ' '), 'api.threats.', ''), params.get('site_id')))
                return Site(result)
        else:
            logger.error('No site_id or rule_id parameter has been passed in.')
    else:
        logger.error('No parameters where applied.')
