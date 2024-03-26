import logging
from ..Utils.executeRest import execute

class Stats:
    def __init__(self, data):
        self.account_id = data.get('account_id') or ''
        self.site_id = data.get('site_id') or ''
        self.time_range = data.get('time_range') or ''
        self.start = data.get('start') or ''
        self.end = data.get('end') or ''
        self.event_type = data.get('event_type') or ''
        self.base_url = 'https://my.incapsula.com' # Can we move this higher?
        self.endpoint = '/api/stats/v1'
        self.log = data.get('log') or 'INFO'

    @staticmethod
    def read(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        param['stats'] = args.event_type
        logging.debug(param)
        resturl = 'https://my.incapsula.com/api/stats/v1'
        response = execute(resturl, param)
        return response

    
    '''
    @staticmethod
    def commit(args):
        param = vars(args)
        # action = param['do']
        # print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/stats/v1'


        result = execute(resturl, param)
        Stats.format_data(result)
        exit(0)
    '''