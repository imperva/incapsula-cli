from Utils.executeRest import execute
from Utils.incapError import IncapError
import logging
from Utils.print_table import PrintTable
from Utils.table_formatter import TableFormatter
from Sites.site import Site


class DataCenter:
    def __init__(self, data):
        self.id = data['id']
        self.enabled = data['enabled']
        self.servers = data['servers']
        self.name = data['name']
        self.contentOnly = data['contentOnly']

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = '{}/{}'.format(str.replace(__name__[0].lower() + __name__[1:], '.', '/'), action)

        if action == 'list':
            result = execute(resturl, param)
            DataCenter._list(result)
            return result
        else:
            result = execute(resturl, param)
            DataCenter._result(execute(result, action))
            return result

    @staticmethod
    def get_data_centers(param):
        print('Get site data centers.')
        resturl = '{}/{}'.format(str.replace(__name__[0].lower() + __name__[1:], '.', '/'), param['do'])
        return execute(resturl, param)

    @staticmethod
    def _result(result, action):
        if result.get('res') != '0':
            err = IncapError(result)
            err.log()
            return err
        else:
            print('{} successful on data center ID: {}'.format(action[0].upper() + action[1:], result['datacenter_id']))

    @staticmethod
    def _list(result):
        if int(result.get('res')) != 0:
            err = IncapError(result)
            err.log()
            return err
        else:
            for dcs in result['DCs']:
                DataCenter.print_data_center([dcs])

    @staticmethod
    def print_data_center(dc: list):
        format_site = TableFormatter(headers=['id', 'enabled', 'name', 'contentOnly', 'servers'], data=dc)
        PrintTable(label='Data Center', data=format_site.headers).print_all()


class Server:
    def __init__(self, data):
        self.id = data['id']
        self.enabled = data['enabled']
        self.address = data['address']
        self.isStandby = data['isStandby']

    @staticmethod
    def servers(args):
        param = vars(args)
        action = param['do']
        print('{} site server'.format(action))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = '{}/{}'.format(str.replace(__name__[0].lower() + __name__[1:], '.', '/') + '/servers', action)

        Server._execute(execute(resturl, param), action)

    @staticmethod
    def _execute(result, action):
        if result.get('res') != '0':
            err = IncapError(result)
            err.log()
            return err
        else:
            print('{} successful on server ID: {}'.format(action[0].upper() + action[1:], result['server_id']))

    def print_servers(self):
        server_header = [['Id', self.id], ['Enabled', self.enabled],
                         ['Address', self.address], ['Standby', self.isStandby]]
        for v in server_header:
            if len(v[0]) > len(v[1]):
                v.append(len(v[0]))
            else:
                v.append(len(v[1]))
        return server_header

