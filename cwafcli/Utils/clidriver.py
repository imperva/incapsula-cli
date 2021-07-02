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
    elif type(response) is dict:
        if args.output == "json":
            print(json.dumps(response, sort_keys=True, indent=4))
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
