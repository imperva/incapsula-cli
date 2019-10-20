import json
import os
import urllib
from urllib import request, parse
from urllib.error import HTTPError, URLError
from socket import timeout
from Config.configuration import IncapConfigurations
import logging
import ssl


def execute(resturl, param, endpoint=""):
    try:
        del param["func"]
        del param["do"]
        del param["log"]
    except:
        pass

    ctx = ssl._create_unverified_context()
    ctx.check_hostname = False

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
        logging.debug('Request Data: {}'.format(param))
        p = ''
        for k, v in param.items():
            p += '{}={}&'.format(k, v)
        logging.debug("curl -d '{}' {}".format(p, endpoint))

        data = urllib.parse.urlencode(param).encode()
        headers = {'content-type': "application/x-www-form-urlencoded"}
        req = urllib.request.Request(endpoint, data, headers, method='POST')

        with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
            result = json.loads(response.read().decode('utf8'))
            logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))
            logging.debug("HTTP Response Code: {}".format(response.getcode()))
            return result

    except (HTTPError, URLError) as error:
        logging.error('Data was not received from %s\nError: %s' % (endpoint, error))
        exit(1)

    except timeout:
        logging.error('Socket timed out - URL %s' % endpoint)
        exit(1)

