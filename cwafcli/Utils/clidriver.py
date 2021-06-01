import argparse
import json
import cwafcli
from ..Config import config_parse
from ..Sites import site_parse
from ..Policies import policy_parse
from ..InfraProtect import infra_parse
from ..Rules import rule_parse
from ..Cache import cache_parse
from ..Accounts import account_parse
from ..Roles import role_parse

parser = argparse.ArgumentParser(prog='incap',
                                 usage='%(prog)s <resource> <command> [options]',
                                 description="CLI for site, account and security CRUD on Incapsula via API.")
parser.add_argument('--api_id', help='API authentication identifier.')
parser.add_argument('--api_key', help='API authentication identifier.')
parser.add_argument('--version', action='version', version=cwafcli.__version__)
parser.add_argument('--profile', default='api', help='Allows for multiple API profiles to be used.')
parser.add_argument('--log', default='INFO', help='Set the log level to DEBUG, WARN, ERROR, CRITICAL; default is INFO.')
parser.add_argument('--output', default='friendly', help='Select json else default is friendly output messages.')
subparsers = parser.add_subparsers()

cli_config_parser = config_parse(subparsers)
account_parser = account_parse(subparsers)
site_parser = site_parse(subparsers)
policy_parser = policy_parse(subparsers)
rule_parser = rule_parse(subparsers)
cache_parser = cache_parse(subparsers)
infra_parser = infra_parse(subparsers)
role_parser = role_parse(subparsers)


def main(args=None):
    import logging
    import requests
    args = parser.parse_args(args=args)
    logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))

    response = args.func(args)

    if type(response) is requests.exceptions.HTTPError:
        logging.error(response)
    elif response:
        if args.output == "json":
            print(json.dumps(response, sort_keys=True, indent=4))
        if args.output == "friendly" and "domain" in response:
            from ..Sites import Site
            Site(response).log(response)
        if args.output == "friendly" and "sites" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['domain', 'status', 'site_id', 'log_level'], data=response['sites'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Sites', data=format_site.headers).print_all()
        if args.output == "friendly" and "delivery_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'action', 'rewrite_name', 'from', 'to'], data=response['delivery_rules']['Rewrite'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Rewrite', data=format_site.headers).print_all()
        if args.output == "friendly" and "custom_error_response_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'error_type', 'error_response_format'], data=response['custom_error_response_rules']['RewriteResponse'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Custom Error Response Rules', data=format_site.headers).print_all()
        if args.output == "friendly" and "Redirect" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'from', 'to', 'response_code'], data=response['delivery_rules']['Redirect'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Redirect', data=format_site.headers).print_all()
        if args.output == "friendly" and "delivery_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'action'], data=response['delivery_rules']['RewriteResponse'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Rewrite Response', data=format_site.headers).print_all()
        if args.output == "friendly" and "delivery_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'from', 'to', 'response_code'], data=response['delivery_rules']['SimplifiedRedirect'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Simplified Redirect', data=format_site.headers).print_all()
        if args.output == "friendly" and "incap_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'action'], data=response['incap_rules']['All'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Security Rules', data=format_site.headers).print_all()
        if args.output == "friendly" and "incap_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'enabled'], data=response['incap_rules']['WafOverride'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='WAF Override', data=format_site.headers).print_all()
        if args.output == "friendly" and "rate_rules" in response:
            from cwafcli.Utils.table_formatter import TableFormatter
            format_site = TableFormatter(headers=['name', 'id', 'filter', 'context', 'interval', 'context', 'enabled'], data=response['rate_rules']['Rates'])
            from cwafcli.Utils.print_table import PrintTable
            PrintTable(label='Rates', data=format_site.headers).print_all()
        else:
            for k, v in sorted(response.items()):
                if type(response[k]) is str:
                    print("{} = {}".format(k.upper(), response[k]))
                elif type(response[k]) is int:
                    print("{} = {}".format(k.upper(), response[k]))
                elif type(response[k]) is dict:
                    for ke, va in response[k].items():
                        print("{} = {}".format(ke.upper(), va))
                elif type(response[k]) is list:
                    for sub in response[k]:
                        if type(sub) is dict:
                            for ke, va in sub.items():
                                if type(va) == list:
                                    for sub in va:
                                        val = ''.join(sub)
                                        print(" {} = {}".format(k.upper(), val))
                                else:
                                    print("{} = {}".format(ke.upper(), va))
                        else:
                            val = ''.join(sub)
                            print("{} = {}".format(k.upper(), val))

def testing(args=None):
    args = parser.parse_args(args=args)
    return args.func(args)
