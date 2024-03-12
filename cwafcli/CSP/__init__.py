import configparser
import json
import os

from cwafcli.CSP.swagger_client import ApiClient, WebsitesApi, Site, Analytics, SetSite
from cwafcli.CSP.swagger_client.rest import ApiException
from cwafcli.CSP.swagger_client import Configuration


def create_subparser(parent_parser, call, method, param, description):
    website_parser = parent_parser.add_parser(call, help=description)
    # Add subcommand-specific arguments
    if param is not None:
        website_parser.add_argument(param, help=description)
    if method == "PUT" or method == "POST":
        website_parser.add_argument("body", help=description)
    website_parser.set_defaults(func=read, do=call)


def read(args):
    params = vars(args)
    config = configure()
    try:
        instance = WebsitesApi(ApiClient(config))
        if params["do"] == "get_sites":
            return Site(instance.get_sites()).to_dict()
        elif params["do"] == "get_site":
            return instance.get_site(params['siteId']).to_dict()
        elif params["do"] == "get_site_reputation":
            return instance.get_site_reputation(params['siteId']).to_dict()
        elif params["do"] == "get_site_settings":
            return instance.get_site_settings(params['siteId']).to_dict()
        elif params["do"] == "get_discovery_status":
            return instance.get_discovery_status(params['siteId']).to_dict()
        elif params["do"] == "get_enforcement_mode":
            mode = instance.get_enforcement_mode(params['siteId'])
            return {"mode": mode}
        elif params["do"] == "get_google_tracking_ids":
            return [Analytics(instance.get_google_tracking_ids(params['siteId'])).to_dict()]
        elif params["do"] == "set_site":
            print(params["body"])
            return instance.set_site(json.loads(params["body"]), params['siteId']).to_dict()
        elif params["do"] == "set_discovery_status":
            discovery_status = instance.set_discovery_status(params["body"], params['siteId'])
            return {"discovery_status": discovery_status}
        elif params["do"] == "set_enforcement_mode":
            mode = instance.set_enforcement_mode(params["body"], params['siteId'])
            return {"mode": mode}
    except ApiException as e:
        print(e)
        return e


def get_params() -> list:
    pwd = os.path.dirname(__file__)
    doc = "docs/WebsitesApi.md"
    abs_path = os.path.join(pwd, doc)
    with open(abs_path, "r") as f:
        lines = f.read()
        needed = lines.split("\n------------- | ------------- | -------------\n")

        line = needed[1].split("\n\n")

        items = line[0].strip().split("\n")

        args_params = []
        for item in items:
            call, method, description = item.split("|")
            if "{" and "}" in method:
                param = method.split("}")[0].split("{")[1]
            else:
                param = None
            call = call.split("**]")[0].split("[**")[1]
            method = method.split("** ")[0].split(" **")[1]
            args_params.append((call, method, param, description))
        return args_params


def configure() -> Configuration:
    from ..Config.configuration import IncapConfigurations
    api_id = os.getenv("IMPV_API_ID", IncapConfigurations.get_config("api", 'id'))
    api_key = os.getenv("IMPV_API_KEY", IncapConfigurations.get_config("api", 'key'))
    config = Configuration()
    config.api_key['x-API-Id'] = api_id
    config.api_key['x-API-Key'] = api_key
    config.verify_ssl = True
    config.debug = False
    return config
