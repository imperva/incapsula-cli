from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging
from Utils.incapResponse import IncapResponse


def u_cachemode(args):
    output = 'Update cache setting on {0} to be {1}.'. format(args.site_id, args.cache_mode)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = {
        "api_id": args.api_id,
        "api_key": args.api_key,
        "site_id": args.site_id,
        "cache_mode": args.cache_mode,
        "dynamic_cache_duration": args.dynamic_cache_duration,
        "aggressive_cache_duration": args.aggressive_cache_duration
    }
    result = update(param)

    if result.get('res') != 0:
        err = IncapError(result)
        err.log()
    else:
        resp = IncapResponse(result)
        print('Updated cache mode to {}'.format(param.get('cache_mode').replace('_', ' ')))
        if param.get('dynamic_cache_duration') != '':
            print('Setting dynamic cache duration to {}'.format(param.get('dynamic_cache_duration').replace('_', ' ')))
        if param.get('aggressive_cache_duration') != '':
            print('Setting aggressive cache duration to {}'.format(param.get('aggressive_cache_duration').replace('_', ' ')))
        resp.log()
        return resp


def update(params):
    resturl = '/api/prov/v1/sites/performance/cache-mode'
    if params:
        if "site_id" in params and "cache_mode" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id or cache_mode parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where applied.')