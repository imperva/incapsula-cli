from cwafcli.Statistics.application import Stats

def statistics_parse(subparsers):
    '''
    Implements the argument parser for statistics API
    '''
    stats_parser = subparsers.add_parser('statistics', help='Used to retrieve statistics.',
        usage='incap [options] statistics <command> [options]')
    

    stats_subparsers = stats_parser.add_subparsers()

    '''
    Statistics Subparser - Application Security
    '''
    stats_application_parser = stats_subparsers.add_parser('application',
        help='Retrieve application security statistics',
        usage='incap [options] statistics application [options]')
    
    stats_application_parser.add_argument('--account_id',
        help='Numeric identifier of the account to operate on. '
            'If not specified, operation will be performed on the account '
            'identified by the authentication parameters.')
    
    stats_application_parser.add_argument('--site_id',
        help='Numeric ID of the site (or sites separated by commas) to get '
            'statistics for. If not specified, aggregate statistics for all '
            'sites in the account specied by the --account-id parameter will '
            ' be returned.',
        default=None)
    
    stats_application_parser.add_argument('--time_range',
        help='Time range to gather statistics for. Uses last_90_days as default',
        default='last_90_days'
        )
    
    stats_application_parser.add_argument('--start',
        help='Used with a custom time range to specify the start time. ',
        default=None)
    
    stats_application_parser.add_argument('--end',
        help='Used with a custom time range to specify the start time. ',
        default=None)
    
    stats_application_parser.add_argument('--event_type',
        help='Specify the event type to be retrieved',
        default=None,
        required=True)
    
    stats_application_parser.set_defaults(func=Stats.read)


    '''
    TODO: Future Work
    stats_infra_parser = stats_subparsers.add_parser(
        'infra',
        help='Retrieve network DDoS Statistics',
        usage='incap [options] statistics account [options] account_id')
    '''