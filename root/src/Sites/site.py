import time
from pprint import pprint
from Sites.cache import Cache
from Integration.clapps import r_clapps
import Utils.log
logger = Utils.log.setup_custom_logger(__name__, fmt='%(message)s')


class Site:
    def __init__(self, data):
        # from pprint import pprint
        # pprint(data)
        self.domain = data.get('domain') or ''
        self.site_id = data.get('site_id') or int
        self.account_id = data.get('account_id') or ''
        self.active = data.get('active') or ''
        self.extended_ddos = data.get('extended_ddos') or int
        self.res = data.get('res') or int
        self.response_message = data.get('res_message') or ''
        self.display_name = data.get('display_name') or ''
        self.acceleration_level = data.get('acceleration_level') or ''
        self.site_creation_date = data.get('site_creation_date') or int
        self.status = data.get('status') or ''
        self.dns = data.get('dns') or []
        self.additionalErrors = data.get('additionalErrors') or []
        self.ips = data.get('ips') or []
        self.debug_info = data.get('debug_info') or []
        self.login_protect = data.get('login_protect') or {}
        self.original_dns = data.get('original_dns') or []
        self.performance_configuration = data.get('performance_configuration') or {}
        self.sealLocation = data.get('sealLocation') or {}
        self.security = data.get('security') or None
        self.siteDualFactorSettings = data.get('siteDualFactorSettings') or {}
        self.ssl = data.get('ssl') or {}
        self.warnings = data.get('warnings') or []
        self.authentication_methods = self.login_protect.get('authentication_methods') or []
        self.incap_rules = data.get('incap_rules') or []
        self.clapps = None
        self.cache = Cache(self.performance_configuration)

    def get_clapps(self, cl_id):
        if self.clapps is None:
            self.clapps = r_clapps()
            client = self.clapps['clientAppTypes'][cl_id[0]] + ' with client name ' + self.clapps['clientApps'][cl_id[0]]
            return client
        else:
            client = self.clapps['clientAppTypes'][cl_id[0]] + ' with client name ' + self.clapps['clientApps'][cl_id[0]]
            return client

    def log(self):
        divide = '-------------------------------------------------------------------------------------------------'
        thistime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.site_creation_date / 1000.0))
        logger.debug(divide)
        logger.debug('Site ID: %s' % self.site_id)
        logger.debug('Domain: %s' % self.domain)
        logger.debug('Display Name = %s' % self.display_name)
        logger.debug('Account ID: %s' % self.account_id)
        logger.debug('Site status: %s' % self.status)
        logger.debug('Site Creation Date: %s' % thistime)
        logger.debug('Active Status = %s' % self.active)
        logger.debug('Extended DDoS = %s' % self.extended_ddos)
        logger.debug('Seal Location = %s' % self.sealLocation['name'])
        logger.debug('Acceleration Level: %s' % self.acceleration_level)

        logger.debug(divide)
        logger.debug('Current DNS information is set to the following:')
        logger.debug(divide)
        for dns in self.dns:
            for dns_ip in dns['set_data_to']:
                logger.debug('The current %s Record for %s is %s\r' %
                             (dns['set_type_to'], dns['dns_record_name'], dns_ip))

        logger.debug(divide)
        logger.debug('Original DNS information was set to the following:')
        logger.debug(divide)
        for o_dns in self.original_dns:
            for o_dns_ip in o_dns['set_data_to']:
                logger.debug('The original %s Record for %s was %s\r' %
                      (o_dns['set_type_to'], o_dns['dns_record_name'], o_dns_ip))
        logger.debug(divide)

        if self.additionalErrors:
            logger.debug('Additional Errors:')
            for err in self.additionalErrors:
                logger.error('%s'.join(err))
        else:
            logger.debug("No additional Errors")

        logger.debug(divide)

        for ip in self.ips:
            logger.debug('Origin Server IP/CNAME: %s' % ip)
        logger.debug(divide)
        if self.login_protect.get('enabled'):
            logger.debug('Login Protect details:')
            logger.debug('Allow All Users = %s' % self.login_protect['allow_all_users'])
            logger.debug('Authentication Method(s) = %s.' %
                         ', '.join(self.login_protect['authentication_methods']))
            logger.debug('Send Login Protect Notifications = %s' % self.login_protect['send_lp_notifications'])
            for users in self.login_protect['specific_users_list']:
                logger.debug('Login Protect UserName = {name}, Email = {email} '
                             'and Status = {status}'.format(**users))
            logger.debug('URL(s) = %s' % ', '.join(self.login_protect['urls']))


        #logger.debug('Site Dual Factor Settings = %s' % self.siteDualFactorSettings)
        #logger.debug('SSL = %s' % self.ssl)

        #logger.debug('PerformanceConfiguration = %s' % self.performance_configuration)
        logger.debug(divide)

        if 'acls' in self.security:
            logger.debug('ACL settings are as follows:')
            for aclRules in self.security['acls']['rules']:
                if aclRules['id'] == 'api.acl.blacklisted_ips':
                    logger.debug('The following IPs are blacklisted: %s' % ', '.join(aclRules['ips']))
                    if 'exceptions' in aclRules:
                        logger.debug('Blacklisted IPs Exceptions follow:')

                        for exception in aclRules['exceptions']:
                            self.site_exceptions(exception)

                elif aclRules['id'] == 'api.acl.whitelisted_ips':
                    logger.debug('The following IPs are whitelisted: %s' % ', '.join(aclRules['ips']))

                elif aclRules['id'] == 'api.acl.blacklisted_countries':
                    logger.debug('The following countries are blacklisted: %s' % ', '.join(aclRules['geo']['countries']))
                    if 'exceptions' in aclRules:
                        logger.debug('Blacklisted Countries Exceptions follow:')

                        for exception in aclRules['exceptions']:
                            self.site_exceptions(exception)

                elif aclRules['id'] == 'api.acl.blacklisted_urls':

                    for url in aclRules['urls']:
                        logger.debug('URL is blacklisted: url= %s pattern= %s.'
                                     % (''.join(url['value']), ''.join(url['pattern'])))
                else:
                    logger.debug("Nothing is being blacklisted or whitelisted.")
        else:
            logger.debug(divide)
            logger.debug("No ACLs")
        logger.debug(divide)

        logger.debug('Security settings are as follows:')
        logger.debug(divide)

        for secRule in self.security["waf"]["rules"]:

            if secRule['name'] == 'Bot Access Control':
                logger.debug('{name} setting are: Block Bad Bots={block_bad_bots} '
                             'and Challenge Suspected Bots={challenge_suspected_bots}.'.format(**secRule))

                if 'exceptions' in secRule:
                    logger.debug('Bot Exceptions follow:')

                    for exception in secRule['exceptions']:
                        self.site_exceptions(exception)

            elif secRule['name'] == 'DDoS':
                logger.debug('{name} setting are: DDoS Activation Mode={activation_mode_text} '
                             'and DDoS Traffic Threshold={ddos_traffic_threshold}.'.format(**secRule))

                if 'exceptions' in secRule:
                    logger.debug('DDoS Exceptions follow:')

                    for exception in secRule['exceptions']:
                        self.site_exceptions(exception)
            else:
                logger.debug('{name} is set to {action_text}.'.format(**secRule))

        logger.debug('\nSSL info following:')
        logger.debug('SSL detected: {0}, detected status: {1}.'
                     .format(self.ssl['origin_server']['detected'], self.ssl['origin_server']['detectionStatus']))

        if self.ssl['origin_server']['detected'] == 'True':

            if 'validation_method' in self.ssl['generated_certificate']:
                logger.debug('Validation has been set to {0}.'.format(self.ssl['generated_certificate']['validation_method']))

                if self.ssl['generated_certificate']['validation_method'] == 'dns':

                    for v_data in self.ssl['generated_certificate']['validation_data']:
                        logger.debug('Please set the TXT record for {0} to {1}.'
                              .format(v_data['dns_record_name'], v_data['set_data_to']))
                logger.debug('The SSL certificate status is {0}.'.format(self.ssl['generated_certificate']['validation_status']))
                logger.debug('The CA is {0}.'.format(self.ssl['generated_certificate']['ca']))
                logger.debug('The SAN cert is for {0}.'.format(self.ssl['generated_certificate']['san']))

            else:
                logger.debug('SSL has been detected but no certificate has been created/validated yet.')

        logger.debug('\nWarnings for the following:')

        for warning in self.warnings:
            logger.debug('Warning Type= %s, Set type to= %s, with IP/CNAME=%s'
                  % (warning['type'], warning['set_type_to'], ', '.join(warning['set_data_to'])))
        #logger.debug('Response = %s' % self.res)
        #logger.debug('Response Message = %s' % self.response_message)
        #logger.debug('Debug Info = %s' % self.debug_info)

    def site_exceptions(self, data):
        #logger.debug('{values}'.format(**data))
        for item in data['values']:
            #plogger.debug('{id}'.format(**item))
            if item['id'] == 'api.rule_exception_type.client_ip':
                logger.debug('-------------------------------------------------------------------------------------------\n|\n'
                      '| IP Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ', '.join(item['ips']))
            elif item['id'] == 'api.rule_exception_type.user_agent':
                logger.debug('-------------------------------------------------------------------------------------------\n|\n'
                      '| User Agent Exception ID: {id}'.format(**data) + ' -  Exception for client app type: %s\n|' % ', '.join(item['user_agents']))
            elif item['id'] == 'api.rule_exception_type.url':
                for url in item['urls']:
                    logger.debug('-------------------------------------------------------------------------------------------\n|\n'
                          '| Url Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ''.join(url['value']))
            elif item['id'] == 'api.rule_exception_type.country':
                logger.debug('-------------------------------------------------------------------------------------------\n|\n'
                      '| Country Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ', '.join(item['geo']['countries']))
            elif item['id'] == 'api.rule_exception_type.client_app_id':
                logger.debug('-------------------------------------------------------------------------------------------\n|\n'
                      '| Client Application Exception ID: {id}'.format(**data) + ' - '
                                                                                 'Exception for client app type: %s\n|' % ''.join(self.get_clapps(item['client_apps'])))
