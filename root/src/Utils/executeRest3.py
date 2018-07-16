import json
from urllib.parse import urlencode
import urllib3
from urllib3 import PoolManager, exceptions
from Config.configuration import IncapConfigurations
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def execute(resturl, param):
    config = IncapConfigurations()

    if param.get('api_id') is None:
        param["api_id"] = config.get_api_id()
        if param.get('api_key') is None:
            param["api_key"] = config.get_api_key()
            if param.get('account_id') is None:
                param["account_id"] = config.get_account()

    try:
        print(param)
        data = json.dumps(param)
        headers = {'content-type': "application/x-www-form-urlencoded"}
        response = PoolManager().request_encode_body('POST', str(config.get_baseurl()) + resturl, fields=param,
                                         headers=headers)
        from pprint import pprint
        pprint(response.read())
        return json.loads(response.read().decode('utf8'))

    except exceptions.HTTPError as error:
        logger.debug('Data was not received from %s\nError: %s' % (str(config.baseurl) + resturl, error))
        exit(1)


