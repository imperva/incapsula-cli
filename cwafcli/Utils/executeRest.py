import json
import os
import urllib
from urllib import parse
from ..Config.configuration import IncapConfigurations
import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

endpoint = None


def execute(resturl, param):
    try:
        del param["func"]

    except:
        pass

    if param.get('api_id') is None:
        param["api_id"] = os.getenv("IMPV_API_ID", IncapConfigurations.get_config(param['profile'], 'id'))
        if param.get('api_key') is None:
            param["api_key"] = os.getenv("IMPV_API_KEY", IncapConfigurations.get_config(param['profile'], 'key'))
            if param.get('account_id') is None:
                param["account_id"] = os.getenv("IMPV_ACCOUNT_ID", IncapConfigurations.get_config(param['profile'], 'account'))

    if str(urllib.parse.urlparse(resturl).netloc) == "":
        baseurl = os.getenv("IMPV_BASEURL", IncapConfigurations.get_config(param['profile'], 'baseurl')) or "https://my.imperva.com"
        if not str(urllib.parse.urlparse(baseurl).path).__contains__("/api/prov/v1/"):
            if str(urllib.parse.urlparse(resturl).path).__contains__("/api/integration/v1/clapps"):
                endpoint = baseurl + resturl
            else:
                endpoint = baseurl + "/api/prov/v1/" + resturl

        else:
            if str(urllib.parse.urlparse(resturl).path).__contains__("/api/integration/v1/clapps"):
                endpoint = baseurl.replace("/api/prov/v1/", "/api/integration/v1/clapps")
            else:
                endpoint = baseurl + resturl
    else:
        endpoint = resturl

        if not str(urllib.parse.urlparse(endpoint).scheme) == "https":
            logging.error("Error: URL does not contain the proper scheme 'https'.")

    try:
        logging.debug('Request Data: \n{}'.format(param))
        p = ''
        for k, v in param.items():
            p += '{}={}&'.format(k, v)
        logging.debug("curl -d '{}' {}".format(p, endpoint))

        retry_strategy = Retry(
            total=3,
            status_forcelist=[429],
            method_whitelist=["POST"],
            backoff_factor=2
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)

        with session.post(url=endpoint, data=param, timeout=(5, 15)) as response:
            logging.debug('JSON Response: {}'.format(json.dumps(response.json(), indent=4)))
            return response.json()

    except requests.HTTPError as e:
        logging.error(e)
    except requests.ConnectionError as e:
        logging.error(e)
    except requests.Timeout as e:
        logging.error(e)
    except requests.RequestException as e:
        logging.error(e)
    except requests.exceptions as e:
        logging.error(e)
    exit(1)
