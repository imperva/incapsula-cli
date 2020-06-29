import logging

from ..Utils.executeRest import execute


class Ddos:
    def __init__(self, data):
        self.id = 0

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/v1/infra-protect/test-alerts/ddos/{}'.format(action)
        print(resturl)
        execute(resturl, param)
        #Event.print_data_center(execute(resturl, param)["events"])


class Connection:
    def __init__(self):
        self.id = 0

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/v1/infra-protect/test-alerts/connection/{}'.format(action)
        print(resturl)
        execute(resturl, param)