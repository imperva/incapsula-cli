from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging
from Utils.incapResponse import IncapResponse


def u_cacherule(args):
    output = 'Update cache rules on {0}.'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
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
        resp = IncapResponse(result)
        print('Updated cache rule(s) on site ID: {}'.format(param.get('site_id')))
        for k, v in param.items():

            if len(k) > 10 and len(v) > 0:
                print('Setting {} to {}'.format(k.replace('_', ' '), v))
        resp.log()
        return resp


def update(params):
    resturl = '/api/prov/v1/sites/performance/caching-rules'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')