from Utils.executeRest import execute
import Utils.log
from Utils.incapError import IncapError

logger = Utils.log.setup_custom_logger(__name__)


def u_cacherule(args):
    output = 'Update cache setting on {0}.'. format(args.site_id)
    logger.debug(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "always_cache_resource_url": args.always_cache_resource_url,
        "always_cache_resource_pattern": args.always_cache_resource_pattern,
        "always_cache_resource_duration": args.always_cache_resource_duration,
        "never_cache_resource_url": args.never_cache_resource_url,
        "never_cache_resource_pattern": args.never_cache_resource_pattern,
        "cache_headers": args.cache_headers,
        "clear_always_cache_rules": args.clear_always_cache_rules,
        "clear_never_cache_rules": args.clear_never_cache_rules,
        "clear_cache_headers_rules": args.clear_cache_headers_rules
    }
    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        logger.debug('Result Message: %s' % (result.get('res_message')))


def update(params):
    resturl = '/api/prov/v1/sites/performance/caching-rules'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logger.error('No site ID parameter has been passed in.')
    else:
        logger.error('No parameters where applied.')