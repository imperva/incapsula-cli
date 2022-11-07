from ..Config.configuration import configure


def config_parse(subparsers):
    cli_config_parser = subparsers.add_parser('config', help='Use config to add the default API_ID,'
                                                             ' API_KEY and Account_ID.',
        usage='incap [options] config [options] api_id api_key account_id')
    cli_config_parser.add_argument('api_id', help='API authentication identifier.')
    cli_config_parser.add_argument('api_key', help='API authentication identifier.')
    cli_config_parser.add_argument('account_id', help='Numeric identifier of the account to operate'
                                                      ' on. If not specified, operation will be '
                                                      'performed on the account identified by the '
                                                      'authentication parameters.')
    cli_config_parser.add_argument('--profile', default="api", help='Unique profile when using multiple api ids.')
    cli_config_parser.add_argument('--repo', default='', help='This is optional if you have a '
                                                              'repository where backups and templates can be storied.')
    cli_config_parser.add_argument('--baseurl', default='https://my.imperva.com',
        help='Optionally set the URL for the API domain.')
    cli_config_parser.set_defaults(func=configure)
    return cli_config_parser
