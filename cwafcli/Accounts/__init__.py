from cwafcli.Accounts.account import Account
from cwafcli.Accounts.cAccount import c_account
from cwafcli.Accounts.rAccounts import r_accounts
from cwafcli.Accounts.rAudit import r_audit
from cwafcli.Accounts.rSubAccounts import SubAccount
from cwafcli.Accounts.subscription import r_subscription
from cwafcli.Statistics.stats import Stats


def account_parse(subparsers):
    account_parser = subparsers.add_parser('account',
                                           help='Used to add, delete and configure Incapsula accounts.',
                                           usage='incap [options] account <command> [options]')
    account_subparsers = account_parser.add_subparsers(description='valid subcommands',
                                                       help='additional help')
    account_add_parser = account_subparsers.add_parser('add',
                                                       help='Use this operation to add a new account that '
                                                            'should be managed by the account of the API client '
                                                            '(the parent account). The new account will be configured '
                                                            'according to the preferences set for the '
                                                            'parent account by Incapsula.',
                                                       usage='incap [options] account add [options] email')
    account_add_parser.add_argument('email', help='Email address. For example: "joe@example.com".')
    account_add_parser.add_argument('--parent_id', '--parent_id=', default='',
                                    help='The newly created accounts parent id. '
                                         'If not specified, the invoking account will be assigned as the parent.')
    account_add_parser.add_argument('--user_name', '--user_name=', default='',
                                    help='The account owners name. For example: "John Doe".')
    account_add_parser.add_argument('--plan_id', '--plan_id=', default='',
                                    help='An identifier of the plan to assign to '
                                         'the new account. For example, ent100 for the Enterprise 100 plan.')
    account_add_parser.add_argument('--ref_id', '--ref_id=', default='',
                                    help='Customer specific identifier for this operation.')
    account_add_parser.add_argument('--account_name', '--account_name=', default='', help='Account name.')
    account_add_parser.add_argument('--log_level', '--log_level=<full,security,none,default>', default='',
                                    help='Available only for Enterprise Plan customers that purchased '
                                         'the Logs Integration SKU. Sets the log reporting level for the site. '
                                         'Options are “full”, “security”, “none” and "default"')
    account_add_parser.add_argument('--logs_account_id', default='',
                                    help='Available only for Enterprise Plan customers that purchased the '
                                         'Logs Integration SKU. Numeric identifier of the account that purchased the '
                                         'logs integration SKU and which collects the logs. '
                                         'If not specified, operation will be performed on the account '
                                         'identified by the authentication parameters')
    account_add_parser.set_defaults(func=c_account)

    account_audit_parser = account_subparsers.add_parser('audit',
                                                         help='Use this operation to get audit events for an account.',
                                                         usage='incap [options] account audit [options]')
    account_audit_parser.add_argument('--account_id',
                                      help='Numeric identifier of the account to operate on. If not specified, '
                                           'operation will be performed on the account identified by the authentication'
                                           ' parameters.')
    account_audit_parser.add_argument('--time_range', default='today',
                                      help='Time range to fetch data for. For a detailed description, '
                                           'i.e. last_7_days | last_30_days | last_90_days | month_to_date')
    account_audit_parser.add_argument('--start', default='',
                                      help='Start date in milliseconds since 1970; '
                                           'All dates should be specified as number of milliseconds since midnight 1970 '
                                           '(UNIX time * 1000).')
    account_audit_parser.add_argument('--end', default='', help='End date in milliseconds since 1970; '
                                                                'All dates should be specified as number of milliseconds '
                                                                'since midnight 1970 (UNIX time * 1000).')
    account_audit_parser.add_argument('--type', default='',
                                      help='The api key of the event type, such as audit.account_login.')
    account_audit_parser.add_argument('--page_size', default='50',
                                      help='The number of objects to return in the response. Default: 50.')
    account_audit_parser.add_argument('--page_num', default='0', help='The page to return starting from ..0. Default: 0.')
    account_audit_parser.set_defaults(func=r_audit)

    account_status_parser = account_subparsers.add_parser('status',
                                                          help='Use this operation to get information '
                                                               'about the account of the API client or '
                                                               'one of its managed accounts.',
                                                          usage='incap [options] account status [options]')
    account_status_parser.add_argument('--account_id',
                                       help='Numeric identifier of the account to operate on. If not specified, '
                                            'operation will be performed on the account identified by '
                                            'the authentication parameters.')
    account_status_parser.set_defaults(func=Account.read)
    account_list_parser = account_subparsers.add_parser('list',
                                                        help='Use this operation to get audit events for an account.',
                                                        usage='incap [options] account list [options]')
    account_list_parser.add_argument('--account_id',
                                     help='Numeric identifier of the account to operate on. If not specified, '
                                          'operation will be performed on the account identified by the authentication '
                                          'parameters.')
    account_list_parser.add_argument('--page_size', default='50',
                                     help='The number of objects to return in the response. Default: 50.')
    account_list_parser.add_argument('--page_num', default='0', help='The page to return starting from ..0. Default: 0.')
    account_list_parser.set_defaults(func=r_accounts)

    account_subList_parser = account_subparsers.add_parser('sublist',
                                                           help='Use this operation to get audit events for an account.',
                                                           usage='incap [options] account sublist [options]')
    account_subList_parser.add_argument('--account_id',
                                        help='Numeric identifier of the account to operate on. If not specified, '
                                             'operation will be performed on the account identified by the authentication'
                                             ' parameters.')
    account_subList_parser.add_argument('--page_size', default='50',
                                        help='The number of objects to return in the response. Default: 50.')
    account_subList_parser.add_argument('--page_num', default='0', help='The page to return starting from ..0. Default: 0.')
    account_subList_parser.set_defaults(func=SubAccount.list)

    account_reseller_audit = account_subparsers.add_parser('subscription',
                                                           help='Use this operation to get subscription details for an '
                                                                'account.',
                                                           usage='incap [options] account subscription [options]')
    account_reseller_audit.add_argument('--account_id',
                                        help='Numeric identifier of the account to operate on. If not specified, '
                                             'operation will be performed on the account identified by '
                                             'the authentication parameters.')
    account_reseller_audit.set_defaults(func=r_subscription)

    account_stats_parser = account_subparsers.add_parser('stats',
                                                         help="Use this operation to get site statistics for one or more "
                                                              "sites. This operation may return multiple statistics, "
                                                              "as specified in the stats parameter.",
                                                         usage='incap [options] account stats [options]')
    account_stats_parser.add_argument('--account_id', help='Numeric identifier of the site to operate on.')
    account_stats_parser.add_argument('--time_range', default='today', help="Some operations require the user to specify "
                                                                            "a time range. This is done via the time_range "
                                                                            "parameter, which accepts the following values:"
                                                                            "today,last_7_days,last_30_days,last_30_days,"
                                                                            "month_to_date,custom.")
    account_stats_parser.add_argument('--start', help="	Start date in milliseconds since 1970. "
                                                      "Used together with the time_range parameter "
                                                      "to specify a custom time range.")
    account_stats_parser.add_argument('--end', help="	Start date in milliseconds since 1970. "
                                                    "Used together with the time_range parameter "
                                                    "to specify a custom time range.")
    account_stats_parser.add_argument('stats', help="Statistics to fetch, as specified in the table below. "
                                                    "Multiple statistics can be specified in a comma separated list. "
                                                    "For possible values see below:visits_timeseries,hits_timeseries,"
                                                    "bandwidth_timeseries,requests_geo_dist_summary,visits_dist_summary,"
                                                    "caching,caching_timeseries,threats,incap_rules,"
                                                    "incap_rules_timeseries.")
    account_stats_parser.add_argument('--granularity', help="Statistics to fetch, as specified in the table below. "
                                                            "Multiple statistics can be specified in a comma separated "
                                                            "list. For possible values see below.")
    account_stats_parser.set_defaults(func=Stats.commit)
