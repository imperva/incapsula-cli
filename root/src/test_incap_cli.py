import unittest
import urllib
from urllib import parse
from Utils.incapError import IncapError
from Utils.incapResponse import IncapResponse
from Utils.clidriver import testing
import logging


class TestIncapCLI(unittest.TestCase):
    def setUp(self):
        self.site_id = None

    def test_a_site_add(self):
        print('Add site: www.mooreassistance.net')
        test_incap_cli = testing(['site', 'add', "www.mooreassistance.net"])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to add site: www.mooreassistance.net.')
        TestIncapCLI.site_id = test_incap_cli.site_id

    def test_b_site_list(self):
        print('List sites.')
        test_incap_cli = testing(['site', 'list'])
        self.assertEqual("OK", test_incap_cli.upper(), 'Failed to list sites.')

    def test_c_site_configure(self):
        print('Update site configuration for seal location = bottom right.')
        test_incap_cli = testing(['site', 'configure', 'seal_location', 'api.seal_location.bottom_right',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site configuration.')
        #'--block_bad_bots=false','--challenge_suspected_bots=true', '--activation_mode=on','--ddos_traffic_threshold=100', '--quarantined_urls=/help',

    def test_d_site_set_waf(self):
        print('Update site WAF configuration.')
        rule_ids = ['sql_injection', 'cross_site_scripting', 'illegal_resource_access', 'remote_file_inclusion']
        for rule_id in rule_ids:
            test_incap_cli = testing(['site', 'security', rule_id, '--security_rule_action=block_request',
                                      str(TestIncapCLI.site_id)])
            self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'bot_access_control', '--block_bad_bots=false',
                                  '--challenge_suspected_bots=true', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'backdoor', '--security_rule_action=alert', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'ddos', '--activation_mode=on', '--ddos_traffic_threshold=100',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site WAF configuration.')

    # def test_d_site_waf(self):
    #     print('Update site security configuration.')
    #     test_incap_cli = testing(['site', 'security', 'bot_access_control', '--block_bad_bots=false',
    #                               '--challenge_suspected_bots=true', str(TestIncapCLI.site_id)])
    #     self.assertEqual("OK", test_incap_cli.res_message.upper(), 'The site ID is None.')
    #     test_incap_cli = testing(['site', 'security', 'backdoor', '--security_rule_action=alert', str(TestIncapCLI.site_id)])
    #     self.assertEqual("OK", test_incap_cli.res_message.upper(), 'The site ID is None.')
    #     test_incap_cli = testing(['site', 'security', 'ddos', '--activation_mode=on', '--ddos_traffic_threshold=100',
    #                               str(TestIncapCLI.site_id)])
    #     self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site security configuration.')

    def test_d_site_acl(self):
        print('Update site ACL(security) configuration.')
        test_incap_cli = testing(['site', 'acl', '--urls=/home,index.html', '--url_patterns=prefix,suffix',
                                  'blacklisted_urls', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site ACL(security) configuration.')
        test_incap_cli = testing(['site', 'acl', '--ips=107.232.12.4,102.232.22.99', 'blacklisted_ips',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site ACL(security) configuration.')
        test_incap_cli = testing(['site', 'acl', '--countries=CA,JM,CN', '--continents=AF', 'blacklisted_countries',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site ACL(security) configuration.')
        test_incap_cli = testing(['site', 'acl', '--ips=75.80.36.61', 'whitelisted_ips',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to update site ACL(security) configuration.')

    def test_d_site_waf_exceptions(self):
        print('Update site WAF EXCEPTIONS configuration.')
        rule_ids = ['sql_injection', 'cross_site_scripting', 'illegal_resource_access', 'remote_file_inclusion',
                    'bot_access_control', 'backdoor', 'ddos']
        for rule_id in rule_ids:
            print('Create waf rule exception: {}'.format(rule_id))
            test_incap_cli = testing(['site', 'whitelist', "--urls=/home,/example",  "--countries=JM,CA",
                                      "--continents=AF", "--ips=192.168.1.1,172.21.12.0/24",
                                      "--client_app_types=Browser", "--client_apps=68", "--user_agents=curl",
                                      rule_id, str(TestIncapCLI.site_id)])
            self.assertNotEqual(test_incap_cli, IncapError,
                                'Failed to update site WAF EXCEPTION {} configuration.'.format(rule_id))

    def test_d_site_security_exceptions(self):
        print('Update site ACL(security) EXCEPTIONS configuration.')
        rule_ids = ['blacklisted_countries', 'blacklisted_urls', 'blacklisted_ips']
        for rule_id in rule_ids:
            print('Create security rule exception: {}'.format(rule_id))
            test_incap_cli = testing(['site', 'whitelist', "--urls=/home,/example",  "--countries=JM,CA",
                                      "--continents=AF", "--ips=192.168.1.1,172.21.12.0/24",
                                      "--client_app_types=Browser", "--client_apps=68", "--user_agents=curl",
                                      '--parameters=q,username', rule_id, str(TestIncapCLI.site_id)])
            self.assertEqual("OK", test_incap_cli.res_message.upper(),
                             'Failed to update site ACL(security) EXCEPTION {} configuration.'.format(rule_id))

    def test_y_site_status(self):
        print('Get site status.')
        test_incap_cli = testing(['site', 'status', str(TestIncapCLI.site_id)])
        self.assertNotEqual(test_incap_cli, IncapError, 'Failed to get site status on site ID: {}'.format(TestIncapCLI.site_id))

    def test_z_site_delete(self):
        print('Delete site.')
        test_incap_cli = testing(['site', 'delete', str(TestIncapCLI.site_id)])
        self.assertNotEqual(test_incap_cli, IncapError, 'Failed to delete site on site ID: {}'.format(TestIncapCLI.site_id))


if __name__ == '__main__':
    unittest.main()


