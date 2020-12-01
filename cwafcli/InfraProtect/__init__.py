from cwafcli.InfraProtect.testAlerts import Ddos, Connection
from cwafcli.Statistics.infra import Event


def infra_parse(subparsers):
    infra_parser = subparsers.add_parser('infra',
                                         help='The Test Alerts API enables you to send dummy notifications. \n'
                                              'Many of the parameters are optional. If you do not use them, \n'
                                              'sample data is created automatically based on your existing \n'
                                              'configuration and used to generate the test alerts. \n'
                                              'There is no impact on your actual configuration.',
                                         usage='incap [options] infra <command> [options]')
    infra_subparsers = infra_parser.add_subparsers(description='valid subcommands',
                                                   help='additional help')

    infra_start_ddos_parser = infra_subparsers.add_parser('start', help="Use this operation to list a site's "
                                                                        "data centers including the data centers' servers.",
                                                          usage='incap [options] infra start [options]')
    infra_start_ddos_parser.add_argument('--ip_prefix', default='',
                                         help='The IP prefix to send a notification for. For example, 1.1.1.1.')
    infra_start_ddos_parser.add_argument('--bps', help='Number of bits per second.')
    infra_start_ddos_parser.add_argument('--pps', help='Number of packets per second.')
    infra_start_ddos_parser.set_defaults(func=Ddos.commit, do='start')

    infra_stop_ddos_parser = infra_subparsers.add_parser('stop', help="Use this operation to list a site's "
                                                                      "data centers including the data centers' servers.",
                                                         usage='incap [options] infra stop [options]')
    infra_stop_ddos_parser.add_argument('--ip_prefix', default='',
                                        help='The IP prefix to send a notification for. For example, 1.1.1.1.')
    infra_stop_ddos_parser.add_argument('--bps', help='Number of bits per second.')
    infra_stop_ddos_parser.add_argument('--pps', help='Number of packets per second.')

    infra_stop_ddos_parser.set_defaults(func=Ddos.commit, do='stop')

    infra_up_ddos_parser = infra_subparsers.add_parser('up', help="Use this operation to list a site's "
                                                                  "data centers including the data centers' servers.",
                                                       usage='incap [options] infra up [options]')
    infra_up_ddos_parser.add_argument('--connection_name', default='', help='The connection to send '
                                                                            'a notification for. Enter the '
                                                                            'connection name as it appears '
                                                                            'in the Cloud Security Console’s '
                                                                            'Protection Settings page. For example, '
                                                                            'Test_GRE_Tunnel.')
    infra_up_ddos_parser.set_defaults(func=Connection.commit, do='up')

    infra_down_ddos_parser = infra_subparsers.add_parser('down', help="Use this operation to list a site's "
                                                                      "data centers including the data centers' servers.",
                                                         usage='incap [options] infra down [options]')
    infra_down_ddos_parser.add_argument('--connection_name', default='', help='The connection to send '
                                                                              'a notification for. Enter the '
                                                                              'connection name as it appears '
                                                                              'in the Cloud Security Console’s '
                                                                              'Protection Settings page. For example, '
                                                                              'Test_GRE_Tunnel.')
    infra_down_ddos_parser.set_defaults(func=Connection.commit, do='down')

    infra_events_parser = infra_subparsers.add_parser('events', help="Use this operation to list a site's "
                                                                     "data centers including the data centers' servers.",
                                                      usage='incap [options] infra events [options]')
    infra_events_parser.add_argument('--account_id', help='Numeric identifier of the site to operate on.')
    infra_events_parser.add_argument('--event_type', default='',
                                     help='A comma separated list of specific event types. \n'
                                          'Any of: GRE_TUNNEL_UP, GRE_TUNNEL_DOWN, \n'
                                          'ORIGIN_CONNECTION_GRE_UP, ORIGIN_CONNECTION_GRE_DOWN, \n'
                                          'ORIGIN_CONNECTION_ECX_UP, ORIGIN_CONNECTION_ECX_DOWN, \n'
                                          'ORIGIN_CONNECTION_CROSS_CONNECT_UP, \n'
                                          'ORIGIN_CONNECTION_CROSS_CONNECT_DOWN, DDOS_START_IP_RANGE, \n'
                                          'DDOS_STOP_IP_RANGE, DDOS_QUIET_TIME_IP_RANGE, EXPORTER_NO_DATA, \n'
                                          'EXPORTER_BAD_DATA, EXPORTER_GOOD_DATA, MONITORING_CRITICAL_ATTACK, \n'
                                          'PROTECTED_IP_STATUS_UP, PROTECTED_IP_STATUS_DOWN, \n'
                                          'PER_IP_DDOS_START_IP_RANGE.')
    infra_events_parser.add_argument('--ip_prefix', default='',
                                     help='Specific Protected IP or IP range. For example, 1.1.1.0/24.')
    infra_events_parser.add_argument('--start', default='',
                                     help='Start date in milliseconds since 1970; '
                                          'All dates should be specified as number of milliseconds since midnight 1970 '
                                          '(UNIX time * 1000).')
    infra_events_parser.add_argument('--end', default='', help='End date in milliseconds since 1970; '
                                                               'All dates should be specified as number of milliseconds '
                                                               'since midnight 1970 (UNIX time * 1000).')
    infra_events_parser.add_argument('--page_size', default='50',
                                     help='The number of objects to return in the response. Default: 50.')
    infra_events_parser.add_argument('--page_num', default='0', help='The page to return starting from ..0. Default: 0.')
    infra_events_parser.set_defaults(func=Event.commit, do='events')

    infra_stats_parser = infra_subparsers.add_parser('stats', help="Use this operation to list a site's "
                                                                   "data centers including the data centers' servers.",
                                                     usage='incap [options] infra stats [options]')
    infra_stats_parser.add_argument('--account_id', help='Numeric identifier of the site to operate on.')
    infra_stats_parser.add_argument('--traffic_type', default='',
                                    help='A comma separated list of specific traffic types. \n'
                                         'Any of: UDP, TCP, DNS, DNS_RESPONSE, ICMP, SYN, FRAG, \n'
                                         'LARGE_SYN, NTP, NETFLOW, SSDP, GENERAL. \n'
                                         'Cannot be used together with the pop parameter.')
    infra_stats_parser.add_argument('--traffic', default='', help='Specific traffic. One of: Total, Passed, Blocked.')
    infra_stats_parser.add_argument('--ip_prefix', default='',
                                    help='Specific Protected IP or IP range. For example, 1.1.1.0/24.')
    infra_stats_parser.add_argument('--start', default='',
                                    help='Start date in milliseconds since 1970; '
                                         'All dates should be specified as number of milliseconds since midnight 1970 '
                                         '(UNIX time * 1000).')
    infra_stats_parser.add_argument('--end', default='', help='End date in milliseconds since 1970; '
                                                              'All dates should be specified as number of milliseconds '
                                                              'since midnight 1970 (UNIX time * 1000).')
    infra_stats_parser.add_argument('--pop', default='',
                                    help='A comma separated list of specific PoP names. \n'
                                         'For example: iad, tko. Cannot be used together with the traffic_type parameter.\n'
                                         'For the list of PoP codes and locations, see Incapsula Data Centers (PoPs). ')
    infra_stats_parser.set_defaults(func=Event.commit, do='stats')