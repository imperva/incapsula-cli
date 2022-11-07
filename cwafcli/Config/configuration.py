import configparser
import os
import logging


class IncapConfigurations:
    def __init__(self, api_id=None, api_key=None, account=None, baseurl=None, repo=None, profile=None):
        config = configparser.ConfigParser()
        filename = os.path.expanduser('~') + '/.incap/config.ini'
        config[profile] = {'id': api_id,
                           'key': api_key,
                           'account': account,
                           'baseUrl': baseurl,
                           'repo': repo}
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'a') as configFile:
            config.write(configFile)

    @staticmethod
    def get_config(key, value):
        config = configparser.ConfigParser()
        filename = os.path.expanduser('~') + '/.incap/config.ini'
        config.read(filename)
        config.sections()
        if config:
            try:
                if key in config:
                    return config[key].get(value)
                else:
                    logging.warning('No configuration params found for section={} and key={}.\n'
                                    'Please configure with "incap config -h" or pass in configuration info.'.format(key,
                        value))
                    exit(1)
            except configparser.Error as err:
                logging.error('{}'.format(err))
                logging.error('Please run "incap config" to configure user info')
                return None


def configure(args):
    return IncapConfigurations(api_id=args.api_id, api_key=args.api_key, account=args.account_id,
        baseurl=args.baseurl, repo=args.repo, profile=args.profile)


# def set_context(self, param: dict):
#     print(f'set_context {param}')
#     # if param.get('api_id') is None:
#     self.api_id = os.getenv("IMPV_API_ID", IncapConfigurations.get_config(param['profile'], 'id'))
#     # if param.get('api_key') is None:
#     self.api_key = os.getenv("IMPV_API_KEY", IncapConfigurations.get_config(param['profile'], 'key'))
#     # if param.get('account_id') is None:
#     self.account = os.getenv("IMPV_ACCOUNT_ID", IncapConfigurations.get_config(param['profile'], 'account'))
#     # if param.get('baseurl') is None:
#     self.baseurl = os.getenv("IMPV_BASEURL", IncapConfigurations.get_config(param['profile'], 'baseurl'))
#     # if param.get('repo') is None:
#     self.repo = os.getenv("IMPV_REPO", IncapConfigurations.get_config(param['profile'], 'repo'))
#
# def get_context(self, param: dict):
#     print(f'get_context {param}')
#     if param.get('api_id') is None:
#         self.api_id = os.getenv("IMPV_API_ID", IncapConfigurations.get_config(param['profile'], 'id'))
#         if param.get('api_key') is None:
#             self.api_key = os.getenv("IMPV_API_KEY", IncapConfigurations.get_config(param['profile'], 'key'))
#             if param.get('account_id') is None:
#                 self.account = os.getenv("IMPV_ACCOUNT_ID", IncapConfigurations.get_config(param['profile'], 'account'))


