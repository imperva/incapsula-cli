#!/usr/bin/env python3
'''
Web watcher module
'''
import logging
import logging.handlers
import re
import requests
import time
import urllib3
from requests import HTTPError


class Watcher(object):
    '''
    web site watcher
    '''

    SYS_LOG_MSG_PREFIX = 'url_watcher Smartkey-Alarm: '

    def __init__(self, sys_log_ip, sys_log_port, log_file):
        #self._sys_log = self._get_sys_logger(ip=sys_log_ip, port=sys_log_port)
        self.file_log = self._get_file_logger(file=log_file)

    def _get_sys_logger(self, *, ip, port):
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address=(ip, port))
        logger.addHandler(handler)
        return logger

    def _get_file_logger(self, *, file):
        logger = logging.getLogger(self.__class__.__name__ + ".file_log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(file)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def log(self, msg):
        #sys_log_msg = self.SYS_LOG_MSG_PREFIX + msg
        #self._sys_log.info(sys_log_msg)
        self.file_log.error(msg)

    def check_url(self, url, error_msg, sucess_msg, exp_status_code, header):
        try:
            status_code = requests.get(url, verify=False, headers=header).status_code
            self.file_log.debug("status code for url: {} is: {}".format(url, status_code))
            if status_code != exp_status_code:
                self.log(error_msg)
            else:
                self.file_log.info(sucess_msg)
        except requests.exceptions.SSLError as error:
            self.log(error.strerror)


    def run(self, url, header, status_code, region, service):
        host_header = {'host': header}
        error_msg = f'Smartkey-Alarm: ESK {service} is down in {region}. Please contact Fortanix for support '
        success_msg = f'Smartkey-Alarm: ESK {service} is up {region}'
        exp_status_code = status_code
        self.check_url(url, error_msg, success_msg, exp_status_code, header=host_header)


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    sys_log_ip = '10.202.5.x'
    #sys_log_ip = '10.194.5.x'
    #sys_log_ip = '10.202.9.x'
    sys_log_port = 514
    log_file = '/Users/joe.moore/BitBucket/IncapAPI/root/src/temp files/url_wacher.log'
    watcher = Watcher(sys_log_ip, sys_log_port, log_file)
    ch_www = ('https://107.154.226.17/sys/v1/health', 'www.sit.smartkey.io', 204, 'Chicago', 'Portal')
    ch_ui = ('https://107.154.226.12/health', 'ui.sit.smartkey.io/health', 204, 'Chicago', 'UI')
    ch_apps = ('https://107.154.226.17/sys/v1/health', 'apps.sit.smartkey.io', 204, 'Chicago', 'APPS')
    sv_www = ('https://192.230.100.17/sys/v1/health', 'www.sit.smartkey.io', 204, 'San Jose', 'Portal')
    sv_ui = ('https://192.230.100.12/health', 'ui.sit.smartkey.io/health', 204, 'San Jose', 'UI')
    sv_apps = ('https://192.230.100.17/sys/v1/health', 'apps.sit.smartkey.io', 204, 'San Jose', 'APPS')
    dc_www = ('https://107.154.242.17/sys/v1/health', 'www.sit.smartkey.io', 204, 'Ashburn', 'Portal')
    dc_ui = ('https://107.154.242.12/health', 'ui.sit.smartkey.io', 204, 'Ashburn', 'UI')
    dc_apps = ('https://107.154.242.17/sys/v1/health', 'apps.sit.smartkey.io', 204, 'Ashburn', 'APPS')
    watch = [ch_www, ch_ui, ch_apps, sv_www, sv_ui, sv_apps, dc_www, dc_ui, dc_apps]
    sleep_time = 120  # in seconds
    while True:
        for url, host_name, status_code, region, service in watch:
            watcher.run(url=url,
                        header=host_name,
                        status_code=status_code,
                        region=region,
                        service=service)

