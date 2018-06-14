import json
import requests
from urllib.parse import urlencode
from urllib3 import PoolManager, exceptions
from Config.configuration import IncapConfigurations
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


def execute(resturl, param):
    config = IncapConfigurations()

    if param.get('api_id') is None:
        param["api_id"] = config.get_api_id()
        if param.get('api_key') is None:
            param["api_key"] = config.get_api_key()
            if param.get('account_id') is None:
                param["account_id"] = config.get_account()

    try:
        data = urlencode(param)
        headers = {'content-type': "application/x-www-form-urlencoded"}
        reponse = requests.get
        reponse = PoolManager().request('POST', str(config.get_baseurl()) + resturl + data,
                                        headers=headers, timeout=10)
        return json.loads(reponse.read().decode('utf8'))

    except exceptions.HTTPError as error:
        logger.debug('Data was not received from %s\nError: %s' % (str(config.baseurl) + resturl, error))
        exit(1)


