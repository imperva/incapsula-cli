from cwafcli.Sites.csr import new_csr
from cwafcli.Sites.dCertificate import d_certificate
from cwafcli.Sites.dataCenters import Server, DataCenter
from cwafcli.Sites.site import Site
from cwafcli.Sites.uACL import u_acl
from cwafcli.Sites.uCertificate import u_certificate
from cwafcli.Sites.uWaf import u_security
from cwafcli.Sites.uWhitelist import u_whitelist
from cwafcli.Utils.export import export


def site_parse(subparsers):
    site_parser = subparsers.add_parser('site', help='Used to add, delete and configure Incapsula sites.',
        usage='incap [options] site <command> [options]')
    site_subparsers = site_parser.add_subparsers()
    site_add_parser = site_subparsers.add_parser('add',
        help='Add a new site to an account. '
             'If the site already exists, its status is returned.',
        usage='incap [options] site add [options] domain')
    site_add_parser.add_argument('--account_id',
        help='Numeric identifier of the account to operate on. '
             'If not specified, operation will be performed on the account '
             'identified by the authentication parameters.')

    site_add_parser.add_argument('--ref_id', default='',
        help='Customer specific identifier for this operation.')
    site_add_parser.add_argument('--send_site_setup_emails', default='',
        help='If this value is "false", end users will not get emails about the add site process '
             'such as "DNS instructions" and "SSL setup".')
    site_add_parser.add_argument('--site_ip', default='',
        help='Manually set the web server IP/CNAME. This option is only available '
             'for specific accounts.')
    site_add_parser.add_argument('--force_ssl', default='',
        help='If this value is "true", manually set the site to support SSL. '
             'This option is only available for sites with manually configured IP/CNAME and '
             'for specific accounts.')
    site_add_parser.add_argument('--log_level', default='',
        help='Available only for Enterprise Plan customers that purchased the '
             'Logs Integration SKU. Sets the log reporting level for the site. Options'
             ' are “full”, “security”, “none” and "default"')
    site_add_parser.add_argument('--logs_account_id', default='',
        help='Available only for Enterprise Plan customers that purchased the '
             'Logs Integration SKU. Numeric identifier of the account that purchased the logs'
             ' integration SKU and which collects the logs. If not specified, operation will '
             'be performed on the account identified by the authentication parameters')
    site_add_parser.add_argument('domain', help='The domain name of the site. '
                                                'For example: www.example.com, hello.example.com, example.com')
    site_add_parser.add_argument('--naked_domain_san', default='true', help='Use “true” to add the naked domain '
                                                                            'SAN to a www site’s SSL certificate. '
                                                                            'Default value: true')
    site_add_parser.add_argument('--wildcard_san', default='true', help='Use “true” to add the wildcard SAN '
                                                                        'or “false” to add the full domain SAN to the '
                                                                        'site’s SSL certificate. Default value: true')
    site_add_parser.add_argument('--format', default="text", help='Set the return type to json or text')
    site_add_parser.set_defaults(func=Site.create)

    site_list_parser = site_subparsers.add_parser('list', help='Use this operation to list all sites.',
        usage='incap [options] site list [options]')
    site_list_parser.add_argument('--account_id',
        help='Numeric identifier of the account to operate on. If not specified, '
             'operation will be performed on the account identified '
             'by the authentication parameters.')
    site_list_parser.add_argument('--page_size',
        help='The number of objects to return in the response. Default is 50.')
    site_list_parser.add_argument('--page_num', help='The page to return starting from ..0, Default is 0.')
    site_list_parser.add_argument('--export', default=False, help='Set to true to export files locally.')
    site_list_parser.add_argument('--format', default="text", help='Set the return type to json or text')
    site_list_parser.set_defaults(func=Site.list)

    site_status_parser = site_subparsers.add_parser('status', help='Use this operation to get the status of a site.',
        usage='incap [options] site status [options] site_id')
    site_status_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_status_parser.add_argument('--tests', default='',
        help='List of tests to run on site before returning its status. '
             'A comma separated list of one of: '
             'domain_validation, services, dns. '
             'See detailed description below.')
    site_status_parser.add_argument('--format', default="text", help='Set the return type to json or text')
    site_status_parser.set_defaults(func=Site.read)

    site_delete_parser = site_subparsers.add_parser('delete', help='Use this operation to delete a site.',
        usage='incap [options] site delete site_id')
    site_delete_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_delete_parser.set_defaults(func=Site.delete)

    site_custom_cert_parser = site_subparsers.add_parser('csr', help='Use this operation to create a certificate '
                                                                     'signing request (CSR) for your site. '
                                                                     'For details on how to provide Incapsula with a '
                                                                     'custom certificate without a private key, '
                                                                     'see Upload a Certificate without a Private Key.',
        usage='incap [options] site csr [options] site_id')
    site_custom_cert_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_custom_cert_parser.add_argument('--email', help='Email address. For example: joe@example.com')
    site_custom_cert_parser.add_argument('--organization', help='The legal name of your organization. '
                                                                'This should not be abbreviated or include '
                                                                'suffixes such as Inc., Corp., or LLC.')
    site_custom_cert_parser.add_argument('--organization_unit',
        help='The division of your organization handling the certificate. '
             'For example, "IT Department".')
    site_custom_cert_parser.add_argument('--country',
        help='The two-letter ISO code for the country where your organization is '
             'located.')
    site_custom_cert_parser.add_argument('--state',
        help='The state/region where your organization is located. This should not be '
             'abbreviated.')
    site_custom_cert_parser.add_argument('--city', help='The city where your organization is located.	')
    site_custom_cert_parser.set_defaults(func=new_csr)

    site_upcert_parser = site_subparsers.add_parser('upcert', help='Use this operation to upload custom '
                                                                   'certificate for your site. The following SSL '
                                                                   'certificate file formats are supported:'
                                                                   ' PFX, PEM, CER.',
        usage='incap [options] site upcert [options] certificate site_id')
    site_upcert_parser.add_argument('certificate', help='The certificate file in base64 format (location)')
    site_upcert_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_upcert_parser.add_argument('--private_key', help='The private key of the certificate in base64 format.'
                                                          ' Optional in case of PFX certificate file format')
    site_upcert_parser.add_argument('--passphrase', help='The passphrase used to protect your SSL certificate')
    site_upcert_parser.set_defaults(func=u_certificate)

    site_del_cert_parser = site_subparsers.add_parser('delcert', help='Use this operation to upload custom '
                                                                      'certificate for your site. The following SSL '
                                                                      'certificate file formats are supported:'
                                                                      ' PFX, PEM, CER.',
        usage='incap [options] site upcert [options] certificate site_id')
    site_del_cert_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_del_cert_parser.set_defaults(func=d_certificate)

    site_create_dc_parser = site_subparsers.add_parser('add-dc',
        help="Use this operation to add a data center to a site.",
        usage='incap [options] site add-dc [options] name server_address '
              'site_id')
    site_create_dc_parser.add_argument('name', help="The new data center's name.")
    site_create_dc_parser.add_argument('server_address', help="The server's address. Possible values: IP, CNAME")
    site_create_dc_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_create_dc_parser.add_argument('--is_enabled', help='Enables the data center.')
    site_create_dc_parser.add_argument('--is_content', help='The data center will be available for specific resources '
                                                            '(Forward Delivery Rules).')
    site_create_dc_parser.set_defaults(func=DataCenter.create)

    site_list_dc_parser = site_subparsers.add_parser('list-dc', help="Use this operation to list a site's "
                                                                     "data centers including the data centers' servers.",
        usage='incap [options] site list-dc [options] site_id')
    site_list_dc_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_list_dc_parser.set_defaults(func=DataCenter.list)

    site_update_dc_parser = site_subparsers.add_parser('edit-dc',
        help="Use this operation to edit a site's data center.",
        usage='incap [options] site edit-dc [options] dc_id name')
    site_update_dc_parser.add_argument('site_id', help="The site ID.")
    site_update_dc_parser.add_argument('dc_id', help="The data center's ID.")
    # site_update_dc_parser.add_argument('name', help="The new data center's name.")
    site_update_dc_parser.add_argument('--weight', help='Load-balancing weight of the DC.')
    site_update_dc_parser.add_argument('--is_enabled', help='Enables the data center.')
    site_update_dc_parser.add_argument('--is_standby', help='Enables the data center. '
                                                            'This parameter is deprecated. '
                                                            'Use the is_enabled parameter instead '
                                                            'for the same functionality.')
    site_update_dc_parser.add_argument('--is_content', help='The data center will be available for specific resources '
                                                            '(Forward Delivery Rules).')
    site_update_dc_parser.set_defaults(func=DataCenter.update_v2)

    site_delete_dc_parser = site_subparsers.add_parser('del-dc',
        help="Use this operation to delete a site's data center.",
        usage='incap [options] site del-dc dc_id')
    site_delete_dc_parser.add_argument('dc_id', help="The data center's ID.")
    site_delete_dc_parser.set_defaults(func=DataCenter.delete)

    site_add_server_parser = site_subparsers.add_parser('add-server',
        help="Use this operation to add a server to a data center.",
        usage='incap [options] site add-server [options] server_address '
              'dc_id')
    site_add_server_parser.add_argument('server_address', help="Server IP address.")
    site_add_server_parser.add_argument('dc_id', help="The data center's ID.")
    site_add_server_parser.add_argument('--is_standby', help='Set the server as Active (P0) or Standby (P1) (Boolean).')
    site_add_server_parser.set_defaults(func=Server.servers, do='add')

    site_edit_server_parser = site_subparsers.add_parser('edit-server',
        help="Use this operation to edit a server in a data center.",
        usage='incap [options] site edit-server [options] server_id')
    site_edit_server_parser.add_argument('server_id', help="Server ID.")
    site_edit_server_parser.add_argument('--server_address', help="Server IP address.")
    site_edit_server_parser.add_argument('--is_enabled', help='Enable or disable the server (Boolean).')
    site_edit_server_parser.add_argument('--is_standby',
        help='Set the server as Active (P0) or Standby (P1) (Boolean).')
    site_edit_server_parser.set_defaults(func=Server.servers, do='edit')

    site_delete_server_parser = site_subparsers.add_parser('del-server',
        help="Use this operation to delete a server in a data center.",
        usage='incap [options] site del-server server_id')
    site_delete_server_parser.add_argument('server_id', help="Server ID.")
    site_delete_server_parser.set_defaults(func=Server.servers, do='delete')

    site_configure_parser = site_subparsers.add_parser('configure',
        help='Use this operation to change one of the basic '
             'configuration settings of the site.',
        usage='incap [options] site configure [options] param value site_id')
    site_configure_parser.add_argument('param', help='According to the param value, see table below.')
    site_configure_parser.add_argument('value', help='Name of configuration parameter to set.')
    site_configure_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_configure_parser.set_defaults(func=Site.update)

    site_security_parser = site_subparsers.add_parser('security',
        help='Use this operation to change the security '
             'configuration of a site. To modify the configuration for '
             'a specific rule, additional parameters may be required, as '
             'documented below.',
        usage='incap [options] site security [options] rule_id site_id')
    site_security_parser.add_argument('rule_id', help='ID of the security rule to change. \nFor possible values,'
                                                      ' see the security section in the Get site status API call.\n'
                                                      'bot_access_control, sql_injection, cross_site_scripting,'
                                                      'illegal_resource_access, ddos, or backdoor.')
    site_security_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_security_parser.add_argument('--block_bad_bots', '--block_bad_bots=< true,false>', default='',
        help='Whether or not to block bad bots. Possible values: true, false')
    site_security_parser.add_argument('--challenge_suspected_bots', '--challenge_suspected_bots=<true,false>',
        default='',
        help='Whether or not to send a challenge to clients that are '
             'suspected to be bad bots (CAPTCHA for example). Possible values: true, false')
    site_security_parser.add_argument('--activation_mode', default='',
        help='DDOS activation mode - For example, for "off", use '
             'activation_mode=off.')
    site_security_parser.add_argument('--security_rule_action', default='',
        help='The action that should be taken when a threat is detected, '
             'for example: block_ip, disabled, alert, block_user, block_ip, quarantine_url. '
             'Different actions are allowed per different threats,'
             ' e.g. backdoors may only be quarantined, ignored, or trigger an alert.'
             ' For possible values see the security_rule_action table below.')
    site_security_parser.add_argument('--quarantined_urls', default='',
        help='A comma separated list of encoded URLs to be kept in quarantine. '
             '--quarantined_urls=<str>')
    site_security_parser.add_argument('--ddos_traffic_threshold', default='',
        help='Consider site to be under DDoS if the request rate is above this threshold. '
             'The valid values are 10, 20, 50, 100, 200, '
             '500, 750, 1000, 2000, 3000, 4000, 5000. i.e. --ddos_traffic_threshold=<10')
    site_security_parser.set_defaults(func=u_security)

    site_acl_parser = site_subparsers.add_parser('acl',
        help='Use this operation to change ACL configuration of a site.\n'
             'To modify the configuration for a specific ACL rule, '
             'its values are required, as documented below.\n'
             'string as the list values.',
        usage='incap [options] site acl [options] rule_id site_id')
    site_acl_parser.add_argument('rule_id', help='The id of the acl, e.g blacklisted_ips, blacklisted_countries,'
                                                 ' blacklisted_urls, blacklisted_ips, whitelisted_ips')
    site_acl_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_acl_parser.add_argument('--urls', default='',
        help='A comma separated list of resource paths. Yes For example,'
             ' /home and /admin/index.html are resource paths, however http://www.example.com/home'
             ' is not. Each URL should be encoded separately using percent encoding as '
             'specified by RFC 3986 (http://tools.ietf.org/html/rfc3986#section- 2.1). '
             'An empty URL list will remove all URLs.')
    site_acl_parser.add_argument('--url_patterns', default=None,
        help='A comma separated list of url patterns, one Yes of: '
             'contains | equals | prefix | suffix | not_equals | not_contain | '
             'not_prefix | not_suffix. The patterns should be in accordance with the '
             'matching urls sent by the urls parameter.')
    site_acl_parser.add_argument('--countries', default='', help='A comma separated list of country codes')
    site_acl_parser.add_argument('--continents', default='', help='A comma separated list of continent codes')
    site_acl_parser.add_argument('--ips', default='', help='A comma separated list of IPs or IP ranges, '
                                                           'e.g: 192.168.1.1, 192.168.1.1- 192.168.1.100 or 192.168.1.1/24')
    site_acl_parser.set_defaults(func=u_acl)

    site_whitelist_parser = site_subparsers.add_parser('whitelist', help='Use this operation to set whitelists '
                                                                         'to security rules or ACLs. '
                                                                         'To update an existing whitelist, '
                                                                         'send its ID in the id parameter. '
                                                                         'If the id parameter does not exist a '
                                                                         'new whitelist will be created.',
        usage='incap [options] site whitelist [options] rule_id site_id')
    site_whitelist_parser.add_argument('rule_id', help='Numeric identifier of the rule to get.')
    site_whitelist_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_whitelist_parser.add_argument('--whitelist_id', default='',
        help='The id (an integer) of the whitelist to be set. '
             'This field is optional - '
             'in case no id is supplied, a new whitelist will '
             'be created.')
    site_whitelist_parser.add_argument('--delete_whitelist', default='',
        help='An optional boolean parameter, in case it is set to "true" '
             'and a whitelist id is sent, then the whitelist will be deleted.')
    site_whitelist_parser.add_argument('--urls', default='',
        help='A comma separated list of resource paths. '
             'Yes For example, /home and /admin/index.html are resource paths, '
             'however http://www.example.com/home is not. '
             'Each URL should be encoded separately using percent encoding as '
             'specified by RFC 3986 (http://tools.ietf.org/html/rfc3986#section- 2.1).'
             ' An empty URL list will remove all URLs.')
    site_whitelist_parser.add_argument('--countries', default='', help='A comma separated list of country codes')
    site_whitelist_parser.add_argument('--continents', default='', help='A comma separated list of continent codes')
    site_whitelist_parser.add_argument('--ips', default='', help='A comma separated list of IPs or IP ranges,'
                                                                 ' e.g: 192.168.1.1, 192.168.1.1- 192.168.1.100 '
                                                                 'or 192.168.1.1/24')
    site_whitelist_parser.add_argument('--client_app_types', default='',
        help='A comma separated list of client application types.')
    site_whitelist_parser.add_argument('--client_apps', default='',
        help='Comma separated list of client application ids.')
    site_whitelist_parser.add_argument('--parameters', default='', help='Comma separated list of encoded parameters.')
    site_whitelist_parser.add_argument('--user_agents', default='', help='Comma separated list of encoded user agents.')
    site_whitelist_parser.set_defaults(func=u_whitelist)

    site_export_parser = site_subparsers.add_parser('export', help='Use this operation to export a site or all sites.',
        usage='incap [options] site export')
    site_export_parser.add_argument('--account_id',
        help='Numeric identifier of the account to operate on. '
             'If not specified, operation will be performed on the account '
             'identified by the authentication parameters.')
    site_export_parser.add_argument('--site_id', help='The specific site you would like to export.')
    site_export_parser.add_argument('--path', help='The directory to export to.')
    site_export_parser.add_argument('--filename', default="{site_id}_{domain}_{date}",
        help='If export is selected, you can specify the file name.'
             'Default name is {site_id}_{domain}_{date}.\r'
             'Optional files name:\r'
             '{site_id}_{domain}\r'
             '{site_id}\r'
             '{domain}\r'
             '{site_id}_{domain}_CUSTOM -- Ex: {site_id}_{domain}_Rev3_0B')
    site_export_parser.set_defaults(func=export)

    site_restore_parser = site_subparsers.add_parser('restore', help='Use this operation to bulk add sites.',
        usage='incap [options] site restore [options] path')
    site_restore_parser.add_argument('--account_id',
        help='Numeric identifier of the account to operate on. '
             'If not specified, operation will be performed on the account '
             'identified by the authentication parameters.')
    site_restore_parser.add_argument('--domain', default=None, help='The new domain/site you would like to add.')
    site_restore_parser.add_argument('path', help='The file or directory with multiple files.')
    site_restore_parser.set_defaults(func=export)
