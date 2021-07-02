from cwafcli.Rules.rules import Rules
from cwafcli.Sites.incapRules import IncapRule


def rule_parse(subparsers):
    cache_parser = subparsers.add_parser('rule', help='Used to add, delete and configure rules.',
        usage='incap [options] rule <command> [options]')
    subparsers = cache_parser.add_subparsers()
    add_rule_parser = subparsers.add_parser('add-rule',
        help='Use this operation to add a rule (Simplified Redirect/Redirect/Rates/Security/Rewrite '
             'Request/Forward/Rewrite Response).',
        usage='incap [options] site add-rule [options] site_id')
    add_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    add_rule_parser.add_argument('json')
    # add_rule_parser.add_argument('--name', default='', help='Rule Name')
    # add_rule_parser.add_argument('--action', default='',
    #     help='Rule action. [ RULE_ACTION_REDIRECT, RULE_ACTION_SIMPLIFIED_REDIRECT, '
    #          'RULE_ACTION_REWRITE_URL, RULE_ACTION_REWRITE_HEADER, RULE_ACTION_REWRITE_COOKIE,'
    #          ' RULE_ACTION_DELETE_HEADER, RULE_ACTION_DELETE_COOKIE, '
    #          'RULE_ACTION_RESPONSE_REWRITE_HEADER, RULE_ACTION_RESPONSE_DELETE_HEADER, '
    #          'RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE, RULE_ACTION_FORWARD_TO_DC, '
    #          'RULE_ACTION_FORWARD_TO_PORT, RULE_ACTION_ALERT, RULE_ACTION_BLOCK, '
    #          'RULE_ACTION_BLOCK_USER, RULE_ACTION_BLOCK_IP, RULE_ACTION_RETRY, '
    #          'RULE_ACTION_INTRUSIVE_HTML, RULE_ACTION_CAPTCHA, RULE_ACTION_RATE, '
    #          'RULE_ACTION_CUSTOM_ERROR_RESPONSE ]')
    # add_rule_parser.add_argument('--filter', default='',
    #     help='The filter defines the conditions that trigger the rule action. For action '
    #          'RULE_ACTION_SIMPLIFIED_REDIRECT filter is not relevant. For other actions, '
    #          'if left empty, the rule is always run.')
    # add_rule_parser.add_argument('--response_code', default='',
    #     help="For RULE_ACTION_REDIRECT or RULE_ACTION_SIMPLIFIED_REDIRECT rule's response code, "
    #          "valid values are 302, 301, 303, 307, 308. For "
    #          "RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE rule's response code, valid values are "
    #          "all 3-digits numbers. For RULE_ACTION_CUSTOM_ERROR_RESPONSE, valid values are [ "
    #          "400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, "
    #          "416, 417, 419, 420, 422, 423, 424, 500, 501, 502, 503, 504, 505, 507 ]")
    # add_rule_parser.add_argument('--add_missing', default='',
    #     help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
    # add_rule_parser.add_argument('--from', default='',
    #     help='Pattern to rewrite. For RULE_ACTION_REWRITE_URL - Url to rewrite. For '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value to '
    #          'rewrite. For RULE_ACTION_REWRITE_COOKIE - Cookie value to rewrite')
    # add_rule_parser.add_argument('--to', default='',
    #     help='Pattern to change to. RULE_ACTION_REWRITE_URL - Url to change to. '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value to '
    #          'change to. RULE_ACTION_REWRITE_COOKIE - Cookie value to change to')
    # add_rule_parser.add_argument('--rewrite_name', default='',
    #     help='Name of cookie or header to rewrite. Applies only for RULE_ACTION_REWRITE_COOKIE, '
    #          'RULE_ACTION_REWRITE_HEADER and RULE_ACTION_RESPONSE_REWRITE_HEADER')
    # add_rule_parser.add_argument('--dc_id', default='',
    #     help='Data center to forward request to. '
    #          'Applies only for RULE_ACTION_FORWARD_TO_DC.')
    # add_rule_parser.add_argument('--port_forwarding_context', default='',
    #     help='Context for port forwarding. "Use Port Value" or "Use Header Name". Applies only '
    #          'for RULE_ACTION_FORWARD_TO_PORT')
    # add_rule_parser.add_argument('--port_forwarding_value', default='',
    #     help='Port number or header name for port forwarding. Applies only for '
    #          'RULE_ACTION_FORWARD_TO_PORT')
    # add_rule_parser.add_argument('--rate_context', default='',
    #     help='The context of the rate counter. Possible values IP or Session. Applies only to '
    #          'rules using RULE_ACTION_RATE.')
    # add_rule_parser.add_argument('--rate_interval', default='',
    #     help='The interval in seconds of the rate counter. Possible values is a multiple of 10 '
    #          'minimum 10 maximum 300. Applies only to rules using RULE_ACTION_RATE.')
    # add_rule_parser.add_argument('--error_type', default='',
    #     help='The error that triggers the rule. error.type.all triggers the rule regardless of '
    #          'the error type. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ '
    #          'error.type.all, error.type.connection_timeout, error.type.access_denied, '
    #          'error.type.parse_req_error, error.type.parse_resp_error, '
    #          'error.type.connection_failed, error.type.deny_and_retry, error.type.ssl_failed, '
    #          'error.type.deny_and_captcha, error.type.2fa_required, error.type.no_ssl_config, '
    #          'error.type.no_ipv6_config ]')
    # add_rule_parser.add_argument('--error_response_format', default='',
    #     help='The format of the given error response in the error_response_data field. Applies '
    #          'only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ json, xml ]')
    # add_rule_parser.add_argument('--error_response_data', default='',
    #     help='example: OrderedMap { "incidentId": "$INCIDENT_ID$", "hostName": "$HOST_NAME$", '
    #          '"errorCode": "$RR_CODE$", "description": "$RR_DESCRIPTION$", "timeUtc": '
    #          '"$TIME_UTC$", "clientIp": "$CLIENT_IP$", "proxyId": "$PROXY_ID$", "proxyIp": '
    #          '"$PROXY_IP$" } The response returned when the request matches the filter and is '
    #          'blocked. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE')
    add_rule_parser.set_defaults(func=Rules.create)

    get_rule_parser = subparsers.add_parser('get-rule', help='Use this operation to get a rule.',
        usage='incap [options] site get_rule site_id rule_id')
    get_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    get_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to get.')
    get_rule_parser.set_defaults(func=Rules.read)

    duplicate_rule_parser = subparsers.add_parser('dup-rule', help='Use this operation to duplicate a rule.',
        usage='incap [options] site dup-rule site_id rule_id dup_site_id')
    duplicate_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    duplicate_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to operate on.')
    duplicate_rule_parser.add_argument('dup_site_id', help='Numeric identifier of the site to duplicate operate on.')
    duplicate_rule_parser.set_defaults(func=Rules.duplicate)

    update_rule_parser = subparsers.add_parser('update-rule', help='Use this operation to update rule - must contain '
                                                                   'valid rule id',
        usage='incap [options] site update-rule [options] site_id rule_id')
    update_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    update_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to update.')
    update_rule_parser.add_argument('json')
    # update_rule_parser.add_argument('--name', default='', help='Rule Name')
    # update_rule_parser.add_argument('--action', default='',
    #     help='Rule action. [ RULE_ACTION_REDIRECT, RULE_ACTION_SIMPLIFIED_REDIRECT, '
    #          'RULE_ACTION_REWRITE_URL, RULE_ACTION_REWRITE_HEADER, RULE_ACTION_REWRITE_COOKIE, '
    #          'RULE_ACTION_DELETE_HEADER, RULE_ACTION_DELETE_COOKIE, '
    #          'RULE_ACTION_RESPONSE_REWRITE_HEADER, RULE_ACTION_RESPONSE_DELETE_HEADER, '
    #          'RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE, RULE_ACTION_FORWARD_TO_DC, '
    #          'RULE_ACTION_FORWARD_TO_PORT, RULE_ACTION_ALERT, RULE_ACTION_BLOCK, '
    #          'RULE_ACTION_BLOCK_USER, RULE_ACTION_BLOCK_IP, RULE_ACTION_RETRY, '
    #          'RULE_ACTION_INTRUSIVE_HTML, RULE_ACTION_CAPTCHA, RULE_ACTION_RATE, '
    #          'RULE_ACTION_CUSTOM_ERROR_RESPONSE ]')
    # update_rule_parser.add_argument('--filter', default='',
    #     help='The filter defines the conditions that trigger the rule action. For action '
    #          'RULE_ACTION_SIMPLIFIED_REDIRECT filter is not relevant. For other actions, '
    #          'if left empty, the rule is always run.')
    # update_rule_parser.add_argument('--response_code', default='',
    #     help="For RULE_ACTION_REDIRECT or RULE_ACTION_SIMPLIFIED_REDIRECT rule's response "
    #          "code, valid values are 302, 301, 303, 307, 308. For "
    #          "RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE rule's response code, valid values "
    #          "are all 3-digits numbers. For RULE_ACTION_CUSTOM_ERROR_RESPONSE, valid values "
    #          "are [ 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, "
    #          "414, 415, 416, 417, 419, 420, 422, 423, 424, 500, 501, 502, 503, 504, 505, "
    #          "507 ]")
    # update_rule_parser.add_argument('--add_missing', default='',
    #     help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
    # update_rule_parser.add_argument('--from', default='',
    #     help='Pattern to rewrite. For RULE_ACTION_REWRITE_URL - Url to rewrite. For '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value to '
    #          'rewrite. For RULE_ACTION_REWRITE_COOKIE - Cookie value to rewrite')
    # update_rule_parser.add_argument('--to', default='',
    #     help='Pattern to change to. RULE_ACTION_REWRITE_URL - Url to change to. '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value to '
    #          'change to. RULE_ACTION_REWRITE_COOKIE - Cookie value to change to')
    # update_rule_parser.add_argument('--rewrite_name', default='',
    #     help='Name of cookie or header to rewrite. Applies only for '
    #          'RULE_ACTION_REWRITE_COOKIE, '
    #          'RULE_ACTION_REWRITE_HEADER and RULE_ACTION_RESPONSE_REWRITE_HEADER')
    # update_rule_parser.add_argument('--dc_id', default='',
    #     help='Data center to forward request to. '
    #          'Applies only for RULE_ACTION_FORWARD_TO_DC.')
    # update_rule_parser.add_argument('--port_forwarding_context', default='',
    #     help='Context for port forwarding. "Use Port Value" or "Use Header Name". Applies only '
    #          'for RULE_ACTION_FORWARD_TO_PORT')
    # update_rule_parser.add_argument('--port_forwarding_value', default='',
    #     help='Port number or header name for port forwarding. Applies only for '
    #          'RULE_ACTION_FORWARD_TO_PORT')
    # update_rule_parser.add_argument('--rate_context', default='',
    #     help='The context of the rate counter. Possible values IP or Session. Applies only to '
    #          'rules using RULE_ACTION_RATE.')
    # update_rule_parser.add_argument('--rate_interval', default='',
    #     help='The interval in seconds of the rate counter. Possible values is a multiple of 10 '
    #          'minimum 10 maximum 300. Applies only to rules using RULE_ACTION_RATE.')
    # update_rule_parser.add_argument('--error_type', default='',
    #     help='The error that triggers the rule. error.type.all triggers the rule regardless of '
    #          'the error type. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ '
    #          'error.type.all, error.type.connection_timeout, error.type.access_denied, '
    #          'error.type.parse_req_error, error.type.parse_resp_error, '
    #          'error.type.connection_failed, error.type.deny_and_retry, error.type.ssl_failed, '
    #          'error.type.deny_and_captcha, error.type.2fa_required, error.type.no_ssl_config, '
    #          'error.type.no_ipv6_config ]')
    # update_rule_parser.add_argument('--error_response_format', default='',
    #     help='The format of the given error response in the error_response_data field. Applies '
    #          'only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ json, xml ]')
    # update_rule_parser.add_argument('--error_response_data', default='',
    #     help='example: OrderedMap { "incidentId": "$INCIDENT_ID$", "hostName": "$HOST_NAME$", '
    #          '"errorCode": "$RR_CODE$", "description": "$RR_DESCRIPTION$", "timeUtc": '
    #          '"$TIME_UTC$", "clientIp": "$CLIENT_IP$", "proxyId": "$PROXY_ID$", "proxyIp": '
    #          '"$PROXY_IP$" } The response returned when the request matches the filter and is '
    #          'blocked. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE')
    update_rule_parser.set_defaults(func=Rules.update)

    override_rule_parser = subparsers.add_parser('override-rule', help='Use this operation to override rule - must '
                                                                       'contain valid rule id',
        usage='incap [options] site override-rule [options] site_id rule_id')
    override_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    override_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to update.')
    override_rule_parser.add_argument('json')
    # override_rule_parser.add_argument('--name', default='', help='Rule Name')
    # override_rule_parser.add_argument('--action', default='',
    #     help='Rule action. [ RULE_ACTION_REDIRECT, RULE_ACTION_SIMPLIFIED_REDIRECT, '
    #          'RULE_ACTION_REWRITE_URL, RULE_ACTION_REWRITE_HEADER, '
    #          'RULE_ACTION_REWRITE_COOKIE, '
    #          'RULE_ACTION_DELETE_HEADER, RULE_ACTION_DELETE_COOKIE, '
    #          'RULE_ACTION_RESPONSE_REWRITE_HEADER, RULE_ACTION_RESPONSE_DELETE_HEADER, '
    #          'RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE, RULE_ACTION_FORWARD_TO_DC, '
    #          'RULE_ACTION_FORWARD_TO_PORT, RULE_ACTION_ALERT, RULE_ACTION_BLOCK, '
    #          'RULE_ACTION_BLOCK_USER, RULE_ACTION_BLOCK_IP, RULE_ACTION_RETRY, '
    #          'RULE_ACTION_INTRUSIVE_HTML, RULE_ACTION_CAPTCHA, RULE_ACTION_RATE, '
    #          'RULE_ACTION_CUSTOM_ERROR_RESPONSE ]')
    # override_rule_parser.add_argument('--filter', default='',
    #     help='The filter defines the conditions that trigger the rule action. For action '
    #          'RULE_ACTION_SIMPLIFIED_REDIRECT filter is not relevant. For other actions, '
    #          'if left empty, the rule is always run.')
    # override_rule_parser.add_argument('--response_code', default='',
    #     help="For RULE_ACTION_REDIRECT or RULE_ACTION_SIMPLIFIED_REDIRECT rule's response "
    #          "code, valid values are 302, 301, 303, 307, 308. For "
    #          "RULE_ACTION_RESPONSE_REWRITE_RESPONSE_CODE rule's response code, valid values "
    #          "are all 3-digits numbers. For RULE_ACTION_CUSTOM_ERROR_RESPONSE, valid values "
    #          "are [ 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, "
    #          "414, 415, 416, 417, 419, 420, 422, 423, 424, 500, 501, 502, 503, 504, 505, "
    #          "507 ]")
    # override_rule_parser.add_argument('--add_missing', default='',
    #     help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
    # override_rule_parser.add_argument('--from', default='',
    #     help='Pattern to rewrite. For RULE_ACTION_REWRITE_URL - Url to rewrite. For '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value '
    #          'to rewrite. For RULE_ACTION_REWRITE_COOKIE - Cookie value to rewrite')
    # override_rule_parser.add_argument('--to', default='',
    #     help='Pattern to change to. RULE_ACTION_REWRITE_URL - Url to change to. '
    #          'RULE_ACTION_REWRITE_HEADER/RULE_ACTION_RESPONSE_REWRITE_HEADER - Header value '
    #          'to change to. RULE_ACTION_REWRITE_COOKIE - Cookie value to change to')
    # override_rule_parser.add_argument('--rewrite_name', default='',
    #     help='Name of cookie or header to rewrite. Applies only for '
    #          'RULE_ACTION_REWRITE_COOKIE, RULE_ACTION_REWRITE_HEADER and '
    #          'RULE_ACTION_RESPONSE_REWRITE_HEADER')
    # override_rule_parser.add_argument('--dc_id', default='',
    #     help='Data center to forward request to. '
    #          'Applies only for RULE_ACTION_FORWARD_TO_DC.')
    # override_rule_parser.add_argument('--port_forwarding_context', default='',
    #     help='Context for port forwarding. "Use Port Value" or "Use Header Name". Applies '
    #          'only for RULE_ACTION_FORWARD_TO_PORT')
    # override_rule_parser.add_argument('--port_forwarding_value', default='',
    #     help='Port number or header name for port forwarding. Applies only for '
    #          'RULE_ACTION_FORWARD_TO_PORT')
    # override_rule_parser.add_argument('--rate_context', default='',
    #     help='The context of the rate counter. Possible values IP or Session. Applies only '
    #          'to rules using RULE_ACTION_RATE.')
    # override_rule_parser.add_argument('--rate_interval', default='',
    #     help='The interval in seconds of the rate counter. Possible values is a multiple of '
    #          '10 minimum 10 maximum 300. Applies only to rules using RULE_ACTION_RATE.')
    # override_rule_parser.add_argument('--error_type', default='',
    #     help='The error that triggers the rule. error.type.all triggers the rule regardless '
    #          'of the error type. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ '
    #          'error.type.all, error.type.connection_timeout, error.type.access_denied, '
    #          'error.type.parse_req_error, error.type.parse_resp_error, '
    #          'error.type.connection_failed, error.type.deny_and_retry, '
    #          'error.type.ssl_failed, error.type.deny_and_captcha, error.type.2fa_required, '
    #          'error.type.no_ssl_config, error.type.no_ipv6_config ]')
    # override_rule_parser.add_argument('--error_response_format', default='',
    #     help='The format of the given error response in the error_response_data field. '
    #          'Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE [ json, xml ]')
    # override_rule_parser.add_argument('--error_response_data', default='',
    #     help='example: OrderedMap { "incidentId": "$INCIDENT_ID$", "hostName": '
    #          '"$HOST_NAME$", "errorCode": "$RR_CODE$", "description": "$RR_DESCRIPTION$", '
    #          '"timeUtc": "$TIME_UTC$", "clientIp": "$CLIENT_IP$", "proxyId": "$PROXY_ID$", '
    #          '"proxyIp": "$PROXY_IP$" } The response returned when the request matches the '
    #          'filter and is blocked. Applies only for RULE_ACTION_CUSTOM_ERROR_RESPONSE')
    override_rule_parser.set_defaults(func=Rules.override)

    delete_rule_parser = subparsers.add_parser('del-rule', help='Use this operation to delete a rule.',
        usage='incap [options] site del_rule site_id rule_id')
    delete_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    delete_rule_parser.add_argument('rule_id', help='Numeric identifier of the site to operate on.')
    delete_rule_parser.set_defaults(func=Rules.delete)

    site_add_incaprule_parser = subparsers.add_parser('add_incaprule',
        help='(Legacy, use rule commands) Use this operation to add a '
             'rule (Delivery Rules or IncapRules).',
        usage='incap [options] site add_incaprule [options] site_id')
    site_add_incaprule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_add_incaprule_parser.add_argument('--name', default='', help='Rule Name')
    site_add_incaprule_parser.add_argument('--action', default='',
        help='Rule action. See the possible values in the table below.')
    site_add_incaprule_parser.add_argument('--filter', default='',
        help='Rule will trigger only a request that matches this filter. '
             'For more details on filter guidelines, see Syntax Guide.')
    site_add_incaprule_parser.add_argument('--response_code', default='',
        help="Redirect rule's response code. Valid values are 302, 301, 303, 307, 308.")
    site_add_incaprule_parser.add_argument('--protocol', default='',
        help='')
    site_add_incaprule_parser.add_argument('--add_missing', default='',
        help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
    site_add_incaprule_parser.add_argument('--from', default='',
        help='The pattern to rewrite. '
             'RULE_ACTION_REWRITE_URL - The URL to rewrite. '
             'RULE_ACTION_REWRITE_HEADER - The header value to rewrite. '
             'RULE_ACTION_REWRITE_COOKIE - The cookie value to rewrite.')
    site_add_incaprule_parser.add_argument('--to', default='',
        help='The pattern to change to. '
             'RULE_ACTION_REWRITE_URL - The URL to change to.'
             ' RULE_ACTION_REWRITE_HEADER - The header value to change to. '
             'RULE_ACTION_REWRITE_COOKIE - The cookie value to change to.')
    site_add_incaprule_parser.add_argument('--rewrite_name', default='',
        help='Name of cookie or header to rewrite. '
             'Applies only for RULE_ACTION_REWRITE_COOKIE '
             'and RULE_ACTION_REWRITE_HEADER.')
    site_add_incaprule_parser.add_argument('--dc_id', default='',
        help='Data center to forward request to. '
             'Applies only for RULE_ACTION_FORWARD_TO_DC.')
    site_add_incaprule_parser.add_argument('--is_test_mode', default='',
        help='Make rule apply only for IP address the API request was sent from.')
    site_add_incaprule_parser.add_argument('--lb_algorithm', default='',
        help='Data center load balancing algorithm. Possible values are: '
             'LB_LEAST_PENDING_REQUESTS - Server with least pending requests '
             'LB_LEAST_OPEN_CONNECTIONS - Server with least open connections '
             'LB_SOURCE_IP_HASH - Server by IP hash RANDOM - Random server')
    site_add_incaprule_parser.set_defaults(func=IncapRule.commit, do='add')

    site_list_incaprule_parser = subparsers.add_parser('list_incaprule',
        help='(Legacy, use rule commands) Use this operation to list '
             'rules (Delivery Rules and IncapRules) for a given site.',
        usage='incap [options] site list_incaprule [options] site_id')
    site_list_incaprule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_list_incaprule_parser.add_argument('--include_ad_rules', default='',
        help='Whether or not delivery rules should be included. Defaults to "Yes".')
    site_list_incaprule_parser.add_argument('--include_incap_rules', default='',
        help='Whether or not security rules be included. Defaults to "Yes".')
    site_list_incaprule_parser.add_argument('--page_size', default='',
        help='The number of objects to return in the response. Default is 50.')
    site_list_incaprule_parser.add_argument('--page_num', default='',
        help='The page to return starting from ..0. Default is 0.')
    # site_list_incaprule_parser.set_defaults(func=IncapRule.commit, do='list')
    site_list_incaprule_parser.set_defaults(func=Rules.list)

    site_edit_incaprule_parser = subparsers.add_parser('edit_incaprule',
        help='(Legacy, use rule commands) Use this operation to edit '
             'an existing rule (Delivery Rules or IncapRules).',
        usage='incap [options] site edit_incaprule [options] rule_id')
    site_edit_incaprule_parser.add_argument('rule_id', help='Rule ID.')
    site_edit_incaprule_parser.add_argument('--name', default='', help='Rule Name')
    site_edit_incaprule_parser.add_argument('--action', default='',
        help='Rule action. See the possible values in the table below.')
    site_edit_incaprule_parser.add_argument('--filter', default='',
        help='Rule will trigger only a request that matches this filter. '
             'For more details on filter guidelines, see Syntax Guide.')
    site_edit_incaprule_parser.add_argument('--response_code', default='',
        help='')
    site_edit_incaprule_parser.add_argument('--protocol', default='',
        help='')
    site_edit_incaprule_parser.add_argument('--add_missing', default='',
        help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
    site_edit_incaprule_parser.add_argument('--from', default='',
        help='The pattern to rewrite. '
             'RULE_ACTION_REWRITE_URL - The URL to rewrite. '
             'RULE_ACTION_REWRITE_HEADER - The header value to rewrite. '
             'RULE_ACTION_REWRITE_COOKIE - The cookie value to rewrite.')
    site_edit_incaprule_parser.add_argument('--to', default='',
        help='The pattern to change to. '
             'RULE_ACTION_REWRITE_URL - The URL to change to. '
             'RULE_ACTION_REWRITE_HEADER - The header value to change to. '
             'RULE_ACTION_REWRITE_COOKIE - The cookie value to change to.')
    site_edit_incaprule_parser.add_argument('--rewrite_name', default='',
        help='Name of cookie or header to rewrite. '
             'Applies only for RULE_ACTION_REWRITE_COOKIE '
             'and RULE_ACTION_REWRITE_HEADER.')
    site_edit_incaprule_parser.add_argument('--dc_id', default='',
        help='Data center to forward request to. '
             'Applies only for RULE_ACTION_FORWARD_TO_DC.')
    site_edit_incaprule_parser.add_argument('--is_test_mode', default='',
        help='Make rule apply only for IP address the API request was sent from.')
    site_edit_incaprule_parser.add_argument('--lb_algorithm', default='',
        help='Data center load balancing algorithm. Possible values are:'
             ' LB_LEAST_PENDING_REQUESTS - Server with least pending requests'
             ' LB_LEAST_OPEN_CONNECTIONS - Server with least open connections'
             ' LB_SOURCE_IP_HASH - Server by IP hash'
             ' RANDOM - Random server')
    site_edit_incaprule_parser.set_defaults(func=IncapRule.commit, do='edit')

    site_delete_incaprule_parser = subparsers.add_parser('del_incaprule',
        help='(Legacy, use rule commands) Use this operation to '
             'delete a rule (Delivery Rules or IncapRules).',
        usage='incap [options] site del_incaprule rule_id')
    site_delete_incaprule_parser.add_argument('rule_id', help='Numeric identifier of the site to operate on.')
    site_delete_incaprule_parser.set_defaults(func=IncapRule.commit, do='delete')
