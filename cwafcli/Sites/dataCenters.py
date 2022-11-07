from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.print_table import PrintTable
from ..Utils.table_formatter import TableFormatter
from ..Sites.site import Site


class DataCenter:
    def __init__(self, data):
        self.id = data['id']
        self.enabled = data['enabled']
        self.servers = data['servers']
        self.name = data['name']
        self.contentOnly = data['contentOnly']

    @staticmethod
    def create(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/add".format(**param),
            param, body=param)

    @staticmethod
    def update(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/edit".format(**param),
            param, body=param)

    @staticmethod
    def update_v2(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        print(args)
        body = {
            "DCs": [
                {
                    "dcId": param["dc_id"],
                    "isEnabled": param["is_enabled"],
                    "isStandby": param["is_standby"],
                    "isContent": param["is_content"],
                    "weight": param["weight"]
                }
            ]
        }

        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/origin/datacenters".format(**param),
            param, "POST", body=body)

    @staticmethod
    def list(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/list".format(**param),
            param, body=param)

    @staticmethod
    def delete(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/delete".format(**param),
            param, body=param)

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        resturl = 'sites/dataCenters/{}'.format(action)
        if action == 'list':
            result = execute(resturl, param)
            DataCenter._list(result)
            return result
        else:
            result = execute(resturl, param)
            return result

    @staticmethod
    def get_data_centers(param):
        print('Get site data centers.')
        resturl = '{}/{}'.format(str.replace(__name__, '.', '/').split('/')[1], param['do']).lower()
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
            print(result)
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
    def create(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/servers/add".format(**param),
            param, body=param)

    @staticmethod
    def update(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/servers/edit".format(**param),
            param, body=param)

    @staticmethod
    def delete(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/dataCenters/servers/delete".format(**param),
            param, body=param)

    @staticmethod
    def servers(args):
        param = vars(args)
        action = param['do']
        print('{} site server'.format(action))
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        resturl = 'sites/dataCenters/servers/{}'.format(action)

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
