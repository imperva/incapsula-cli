import json
import urllib
from urllib import request, parse
from urllib.error import HTTPError, URLError
from socket import timeout
from Config.configuration import IncapConfigurations
import logging
import ssl


def execute(resturl, param):

    config = IncapConfigurations()
    ctx = ssl._create_unverified_context()
    ctx.check_hostname = False

    if param.get('api_id') is None:
        param["api_id"] = config.get_api_id()
        if param.get('api_key') is None:
            param["api_key"] = config.get_api_key()
            if param.get('account_id') is None:
                param["account_id"] = config.get_account()

    try:
        logging.debug('Request Data: {}'.format(param))
        data = urllib.parse.urlencode(param).encode()
        headers = {'content-type': "application/x-www-form-urlencoded"}
        req = urllib.request.Request(str(config.get_baseurl()) + resturl, data, headers, method='POST')

        with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
            result = json.loads(response.read().decode('utf8'))
            logging.debug('JSON Response: {}'.format(json.dumps(result, indent=4)))
            return result

    except (HTTPError, URLError) as error:
        logging.error('Data was not received from %s\nError: %s' % (str(config.baseurl) + resturl, error))
        exit(1)

    except timeout:
        logging.error('Socket timed out - URL %s' % str(config.baseurl) + resturl)
        exit(1)

