import json
import os
import urllib
from urllib import parse

import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

endpoint = None


def execute(resturl, param, method=None, body=None):
    global IncapConfigurations
    response = None
    try:
        del param["func"]
    except:
        pass

    if type(body) == dict:
        body = {k: v for k, v in body.items() if v}
        try:
            del body["profile"]
            del body["log"]
            del body["output"]
        except:
            pass
    elif type(body) == str:
        body = json.loads(body)
        try:
            del body["profile"]
            del body["log"]
            del body["output"]
        except:
            pass

    if param.get('api_id') is None:
        from ..Config.configuration import IncapConfigurations
        param["api_id"] = os.getenv("IMPV_API_ID", IncapConfigurations.get_config(param['profile'], 'id'))
        if param.get('api_key') is None:
            param["api_key"] = os.getenv("IMPV_API_KEY", IncapConfigurations.get_config(param['profile'], 'key'))
            if param.get('account_id') is None:
                param["account_id"] = os.getenv("IMPV_ACCOUNT_ID",
                    IncapConfigurations.get_config(param['profile'], 'account'))

    if str(urllib.parse.urlparse(resturl).netloc) == "":
        baseurl = os.getenv("IMPV_BASEURL",
            IncapConfigurations.get_config(param['profile'], 'baseurl')) or "https://my.imperva.com"
        if not str(urllib.parse.urlparse(baseurl).path).__contains__("/api/prov/v1/"):
            logging.debug("baseurl: {}".format(baseurl))
            if str(urllib.parse.urlparse(resturl).path).__contains__("/api/integration/v1/clapps"):
                endpoint = baseurl + resturl
            elif str(urllib.parse.urlparse(baseurl).path).__contains__("/api/prov/v2"):
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

    retry_strategy = Retry(
        total=3,
        status_forcelist=[429],
        backoff_factor=2
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)

    auth = {"api_id": param.pop("api_id"),
            "api_key": param.pop("api_key")
            }

    logging.debug('curl -d "{}" {}?api_id={api_id}&api_key={api_key}'.format(body, endpoint, **auth))

    try:
        if method is None:
            response = session.post(url=endpoint, params=param, timeout=(10, 30),
                headers={'content-type': 'application/x-www-form-urlencoded',
                         'x-API-Id': auth["api_id"],
                         'x-API-Key': auth["api_key"]
                         })
        elif method == "GET":
            response = session.get(url=endpoint, params=body, timeout=(5, 15),
                headers={
                    'accept': 'application/json',
                    'x-API-Id': auth["api_id"],
                    'x-API-Key': auth["api_key"]
                })
        elif method == "POST":
            response = session.post(url=endpoint, json=body, timeout=(5, 15),
                headers={'content-type': 'application/json',
                         'accept': 'application/json',
                         'x-API-Id': auth["api_id"],
                         'x-API-Key': auth["api_key"]
                         })
        elif method == "PUT":
            response = session.put(url=endpoint, json=body, timeout=(5, 15),
                headers={'content-type': 'application/json',
                         'accept': 'application/json',
                         'x-API-Id': auth["api_id"],
                         'x-API-Key': auth["api_key"]
                         })
        elif method == "DELETE":
            response = session.delete(url=endpoint, params=auth, timeout=(5, 15),
                headers={'accept': 'application/json',
                         'x-API-Id': auth["api_id"],
                         'x-API-Key': auth["api_key"]
                         })

        logging.debug(response.request.body)
        logging.debug(json.dumps(response.json(), sort_keys=True, indent=4))
        if response.status_code != 200:
            logging.error(response.text)
            response.raise_for_status()
        elif "res" in response.json() and int(response.json()["res"]) != 0:
            exit(logging.error(
                "Error Code:({res}) - Message:({res_message}) - INFO:({debug_info})".format(**response.json())))
        elif not response.json():
            exit(response.text)
        session.close()
        return response.json()
    except requests.HTTPError as e:
        exit(e)
    except requests.ConnectionError as e:
        exit(e)
    except requests.Timeout as e:
        exit(e)
    except requests.RequestException as e:
        exit(e)
