import json
import unittest
from cwafcli.Utils.incapError import IncapError
from cwafcli.Utils.clidriver import testing


class TestIncapCLI(unittest.TestCase):
    unittest.TestCase.site_id = None
    unittest.TestCase.policy_id = None

    def test_a_site_add(self):
        print('Add site: nobodyknows.dev.impervademo.com')
        test_incap_cli = testing(['--output=json', 'site', 'add', "nobodyknows.dev.impervademo.com", '--force_ssl=true', '--site_ip=198.132.33.2'])
        print(test_incap_cli)
        unittest.TestCase.site_id = test_incap_cli['site_id']
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to add site: nobodyknows.dev.impervademo.com.')

    def test_b_site_list(self):
        print('List sites.')
        test_incap_cli = testing(['--output=json', 'site', 'list'])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to list sites.')

    def test_c_site_set_waf(self):
        print('Update site WAF configuration.')
        rule_ids = ['sql_injection', 'cross_site_scripting', 'illegal_resource_access', 'remote_file_inclusion']
        for rule_id in rule_ids:
            test_incap_cli = testing(['site', 'security', rule_id, '--security_rule_action=block_request',
                                      str(unittest.TestCase.site_id)])
            self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'bot_access_control', '--block_bad_bots=false',
                                  '--challenge_suspected_bots=true', str(unittest.TestCase.site_id)])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'backdoor', '--security_rule_action=alert', str(unittest.TestCase.site_id)])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to update site WAF configuration.')
        test_incap_cli = testing(['site', 'security', 'ddos', '--activation_mode=on', '--ddos_traffic_threshold=100',
                                  str(unittest.TestCase.site_id)])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to update site WAF configuration.')

    def test_d_site_waf_exceptions(self):
        print('Update site WAF EXCEPTIONS configuration.')
        rule_ids = ['sql_injection', 'cross_site_scripting', 'illegal_resource_access', 'remote_file_inclusion',
                    'bot_access_control', 'backdoor', 'ddos']
        for rule_id in rule_ids:
            print('Create waf rule exception: {}'.format(rule_id))
            test_incap_cli = testing(['site', 'whitelist', "--urls=/home,/example",  "--countries=JM,CA",
                                      "--continents=AF", "--ips=192.168.1.1,172.21.12.0/24",
                                      "--client_app_types=Browser", "--client_apps=68", "--user_agents=curl",
                                      rule_id, str(unittest.TestCase.site_id)])
            self.assertNotEqual(test_incap_cli, IncapError,
                                'Failed to update site WAF EXCEPTION {} configuration.'.format(rule_id))

    # def test_e_add_cert(self):
    #     print('Add cert: nobodyknows.dev.impervademo.com')
    #     from time import sleep
    #     sleep(3)
    #     test_incap_cli = testing(['site', 'upcert', '--private_key=/Users/jmoore/Repository/incapsula-cli/certs/dev_impervademo_com.key',
    #                              '/Users/jmoore/Repository/incapsula-cli/certs/dev_impervademo_com.pem',
    #                               str(unittest.TestCase.site_id)])
    #     print(test_incap_cli['res_message'])
    #     self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to upload certificate to:'
    #                                                                ' nobodyknows.dev.impervademo.com.')

    def test_f_site_status(self):
        print('Get site status.')
        test_incap_cli = testing(['--output=json', 'site', 'status', str(unittest.TestCase.site_id)])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to get site status on site ID: {}'.format(unittest.TestCase.site_id))

    def test_g_add_incaprule(self):
        print("Tesing add incapRule.")
        test_incap_cli = testing(['--output=json', 'rule', 'add-rule', '--name=Testing block crawlers', '--action=RULE_ACTION_ALERT', '--filter=ClientType == Crawler', '{}'.format(str(unittest.TestCase.site_id))])
        print(test_incap_cli)
        self.assertGreater(test_incap_cli["rule_id"], 0), 'Failed to add the incapRule on site ID: {}'.format(unittest.TestCase.site_id)

    def test_h_add_policy(self):
        print("Tesing add policy.")
        policy = {
                    "accountId": 2398,
                    "defaultPolicyConfig": [],
                    "description": "Block a list of countries based on attack.",
                    "enabled": True,
                    "name": "Dynamic Country Blocks",
                    "policySettings": [
                      {
                        "data": {
                          "geo": {
                            "continents": [
                              "AS"
                            ],
                            "countries": []
                          }
                        },
                        "policyDataExceptions": [],
                        "policySettingType": "GEO",
                        "settingsAction": "BLOCK"
                      },
                      {
                        "data": {
                          "ips": [
                            "100.64.0.0/16"
                          ]
                        },
                        "policyDataExceptions": [],
                        "policySettingType": "IP",
                        "settingsAction": "BLOCK"
                      },
                      {
                        "data": {
                          "urls": [
                            {
                              "pattern": "EQUALS",
                              "url": "/admin"
                            }
                          ]
                        },
                        "policyDataExceptions": [
                          {
                            "comment": "Blah Blah Blah",
                            "data": [
                              {
                                "exceptionType": "GEO",
                                "values": [
                                  "CA"
                                ]
                              },
                              {
                                "exceptionType": "IP",
                                "values": [
                                  "198.43.121.14"
                                ]
                              },
                              {
                                "exceptionType": "CLIENT_ID",
                                "values": [
                                  "1"
                                ]
                              }
                            ],
                            "exceptionAssetMapping": [],
                          }
                        ],
                        "policySettingType": "URL",
                        "settingsAction": "BLOCK"
                      }
                    ],
                    "policyType": "ACL"
                  }

        test_incap_cli = testing(['policy', 'create', json.dumps(policy)])
        unittest.TestCase.policy_id = test_incap_cli["value"]["id"]
        self.assertGreater(test_incap_cli["value"]["id"], 0), 'Failed to add the incapRule on site ID: {}'.format(unittest.TestCase.site_id)

    def test_i_policy_delete(self):
        print('Delete policy.')
        test_incap_cli = testing(['policy', 'delete', str(unittest.TestCase.policy_id)])
        self.assertEqual(False, test_incap_cli['isError'], 'Failed to delete policy ID: {}'.format(unittest.TestCase.policy_id))

    # def test_y_delete_cert(self):
    #     print('Add site: nobodyknows.dev.impervademo.com')
    #     test_incap_cli = testing(['site', 'delcert', str(unittest.TestCase.site_id)])
    #     print(test_incap_cli)
    #     self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to delete cert: nobodyknows.dev.impervademo.com.')

    def test_z_site_delete(self):
        print('Delete site.')
        test_incap_cli = testing(['site', 'delete', str(unittest.TestCase.site_id)])
        self.assertEqual("OK", test_incap_cli['res_message'].upper(), 'Failed to delete site on site ID: {}'.format(unittest.TestCase.site_id))


if __name__ == '__main__':
    unittest.main()
