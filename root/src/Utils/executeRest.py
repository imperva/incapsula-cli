import json
import os
import urllib
from urllib import request, parse
from urllib.error import HTTPError, URLError
from socket import timeout
from Config.configuration import IncapConfigurations
import logging
import ssl


def execute(resturl, param):
    # with open(os.path.expanduser('~') + '/BitBucket/IncapAPI/root/src/temp files/CEResponse.json', 'r') as json_file:
    #     json_txt = json_file.read()
    #     json_body = json.loads(json_txt)
    #     print(json_body['log'])
    #     exit(0)
    ctx = ssl._create_unverified_context()
    ctx.check_hostname = False

    if param.get('api_id') is None:
        param["api_id"] = IncapConfigurations.get_config(param['profile'], 'id')
        if param.get('api_key') is None:
            param["api_key"] = IncapConfigurations.get_config(param['profile'], 'key')
            if param.get('account_id') is None:
                param["account_id"] = IncapConfigurations.get_config(param['profile'], 'account')
    if "https://" in resturl:
        endpoint = resturl
    else:
        endpoint = IncapConfigurations.get_config(param['profile'], 'baseurl') + resturl

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
            return result

    except (HTTPError, URLError) as error:
        logging.error('Data was not received from %s\nError: %s' % (endpoint, error))
        exit(1)

    except timeout:
        logging.error('Socket timed out - URL %s' % endpoint)
        exit(1)

