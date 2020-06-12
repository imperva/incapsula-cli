import unittest
from .Utils.incapError import IncapError
from .Utils.clidriver import testing


class TestIncapCLI(unittest.TestCase):
    def setUp(self):
        self.site_id = None

    def test_a_site_add(self):
        print('Add site: nobodyknows.dev.impervademo.com')
        test_incap_cli = testing(['site', 'add', "nobodyknows.dev.impervademo.com", '--force_ssl=true'])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to add site: nobodyknows.dev.impervademo.com.')
        TestIncapCLI.site_id = test_incap_cli.site_id

    def test_b_site_list(self):
        print('List sites.')
        test_incap_cli = testing(['site', 'list'])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to list sites.')

    def test_c_site_set_waf(self):
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

    def test_e_add_cert(self):
        print('Add cert: nobodyknows.dev.impervademo.com')
        test_incap_cli = testing(['site', 'upcert', '--private_key=/Users/jmoore/Repo/incapsula-cli/cwafcli/STAR_dev_impervademo_com.key',
                                 '/Users/jmoore/Repo/incapsula-cli/cwafcli/STAR_dev_impervademo_com.crt',
                                  str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to upload certificate to:'
                                                                   ' nobodyknows.dev.impervademo.com.')

    def test_f_site_status(self):
        print('Get site status.')
        test_incap_cli = testing(['site', 'status', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to get site status on site ID: {}'.format(TestIncapCLI.site_id))

    def test_y_delete_cert(self):
        print('Add site: nobodyknows.dev.impervademo.com')
        test_incap_cli = testing(['site', 'delcert', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to delete cert: nobodyknows.dev.impervademo.com.')

    def test_z_site_delete(self):
        print('Delete site.')
        test_incap_cli = testing(['site', 'delete', str(TestIncapCLI.site_id)])
        self.assertEqual("OK", test_incap_cli.res_message.upper(), 'Failed to delete site on site ID: {}'.format(TestIncapCLI.site_id))


if __name__ == '__main__':
    unittest.main()
