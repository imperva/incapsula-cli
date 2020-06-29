from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.incapResponse import IncapResponse


class cacheMode:
    def __init__(self, data):
        self.cache_mode = data['cache_mode']

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/prov/v1/sites/performance/{}'.format(action)

        if action == 'cache-mode/get':
            logging.info('Getting the cache-mode for site-id: {}'.format(param['site_id']))
            result = execute(resturl, param)
            cacheMode._get(result)
            return result
        else:
            logging.info('Setting the cache-mode for site-id: {} to {}.'.format(param['site_id'], param['cache_mode']))
            result = execute(resturl, param)
            return result

    @staticmethod
    def _get(result):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
            return err
        else:
            logging.info('Cache Mode is set to {}.'.format(result.get('cache_mode')))

    @staticmethod
    def _result(result, action):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
            return err
        else:
            print('Successful set site cache mode.')

# def u_cachemode(args):
#     output = 'Update cache setting on {0} to be {1}.'. format(args.site_id, args.cache_mode)
#     logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
#     print(output)
#     param = {
#         "api_id": args.api_id,
#         "api_key": args.api_key,
#         "site_id": args.site_id,
#         "cache_mode": args.cache_mode,
#         "dynamic_cache_duration": args.dynamic_cache_duration,
#         "aggressive_cache_duration": args.aggressive_cache_duration
#     }
#     result = update(param)
#
#     if int(result.get('res')) != 0:
#         err = IncapError(result)
#         err.log()
#     else:
#         resp = IncapResponse(result)
#         print('Updated cache mode to {}'.format(param.get('cache_mode').replace('_', ' ')))
#         if param.get('dynamic_cache_duration') != '':
#             print('Setting dynamic cache duration to {}'.format(param.get('dynamic_cache_duration').replace('_', ' ')))
#         if param.get('aggressive_cache_duration') != '':
#             print('Setting aggressive cache duration to {}'.format(param.get('aggressive_cache_duration').replace('_', ' ')))
#         resp.log()
#         return resp
#
#
# def update(params):
#     resturl = 'sites/performance/cache-mode'
#     if params:
#         if "site_id" in params and "cache_mode" in params:
#             return execute(resturl, params)
#         else:
#             logging.warning("No site_id or cache_mode parameter has been passed in for %s." % __name__)
#     else:
#         logging.error('No parameters where applied.')