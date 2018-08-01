import configparser
import os
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class IncapConfigurations:
    def __init__(self, api_id=None, api_key=None, account=None, baseUrl=None):
        config = configparser.ConfigParser()
        home = os.path.expanduser('~')
        filename = home + '/.incap/config.ini'
        if api_key is None and api_key is None and account is None:
            try:
                config.read(filename)
                config.sections()
                if config:
                    self.api_id = config.get('api', 'id')
                    self.api_key = config.get('api', 'key')
                    self.account = config.get('api', 'account')
                    self.baseurl = config.get('api', 'baseUrl')
            except configparser.Error as err:
                logger.error('{}'.format(err.message))
                exit(1)
        else:
            config['api'] = {'id': api_id,
                             'key': api_key,
                             'account': account,
                             'baseUrl': baseUrl}
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as configFile:
                config.write(configFile)

    def get_api_id(self):
        return self.api_id

    def get_api_key(self):
        return self.api_key

    def get_baseurl(self):
        return self.baseurl

    def get_account(self):
        return self.account


def configure(args):
    return IncapConfigurations(api_id=args.api_id, api_key=args.api_key, account=args.account_id,
                               baseUrl=args.baseUrl)

