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
parser.add_argument('--log', default='INFO')
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
    some = args.func(args)

    if type(some) is requests.exceptions.HTTPError:
        logging.error(some)
    elif type(some) is str:
        logging.info(some)
    elif type(some) is list:
        for sub in some:
            if type(sub) is dict:
                for ke, va in sub.items():
                    print("{} = {}".format(ke.upper(), va))
    else:
        logging.debug(json.dumps(some))
        for k, v in some.items():
            if type(some[k]) is str:
                print("{} = {}".format(k.upper(), some[k]))
            elif type(some[k]) is int:
                print("{} = {}".format(k.upper(), some[k]))
            elif type(some[k]) is dict:
                for ke, va in some[k].items():
                    print("{} = {}".format(ke.upper(), va))
            elif type(some[k]) is list:
                for sub in some[k]:
                    if type(sub) is dict:
                        for ke, va in sub.items():
                            print("{} = {}".format(ke.upper(), va))
                    else:
                        print("{} = {} ".format(k.upper(), sub))
    # if args.log == "DEBUG":
    #     import json
    #     res_json = json.dumps(some)
    #     print(res_json)
    # else:
    #     print(some)


def testing(args=None):
    args = parser.parse_args(args=args)
    return args.func(args)
