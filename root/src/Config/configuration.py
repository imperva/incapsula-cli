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
        try:
            config.read(filename)
            config.sections()
            if config:
                return config.get(key, value)
        except configparser.Error as err:
            logging.error('{}'.format(err.message))
            logging.error('Please run "incap config" to configure user info')
            exit(1)


def configure(args):
    return IncapConfigurations(api_id=args.api_id, api_key=args.api_key, account=args.account_id,
                               baseurl=args.baseurl, repo=args.repo, profile=args.profile)

