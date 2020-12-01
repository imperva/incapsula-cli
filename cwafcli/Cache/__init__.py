from cwafcli.Cache.cache import CacheSettings, CacheRule, DeliverySettings
from cwafcli.Sites.cacheMode import cacheMode
from cwafcli.Sites.uAdvanced import u_advanced
from cwafcli.Sites.uCachingRules import u_cacherule


def cache_parse(subparsers):
    cache_parser = subparsers.add_parser('cache', help='Used to add, delete and configure cache settings, rules and '
                                                       'delivery.',
        usage='incap [options] cache <command> [options]')
    cache_subparsers = cache_parser.add_subparsers()
    site_get_cache_mode_parser = cache_subparsers.add_parser('get-cache-mode', help='Use this operation to get the '
                                                                                    'site cache mode settings.',
        usage='incap [options] site get-cache-mode [options] site_id')
    site_get_cache_mode_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_get_cache_mode_parser.set_defaults(func=cacheMode.commit, do='cache-mode/get')

    site_cache_mode_parser = cache_subparsers.add_parser('edit-cache-mode', help='Use this operation to modify the '
                                                                                 'site cache mode settings.',
        usage='incap [options] site edit-cache-mode [options] cache-mode '
              'site_id')
    site_cache_mode_parser.add_argument('cache_mode', help='disable | static_only | static_and_dynamic | aggressive : '
                                                           'default Static_Only.')
    site_cache_mode_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_cache_mode_parser.add_argument('--dynamic_cache_duration', default='',
        help="Profile dynamic pages and cache duration, pass number followed by"
             " '_' and one of: hr | min | sec | days | weeks: default: 5_min.")
    site_cache_mode_parser.add_argument('--aggressive_cache_duration', default='',
        help="Cache resource duration, pass number followed by"
             " '_' and one of: hr | min | sec | days | weeks: default: 1_hr.")
    site_cache_mode_parser.set_defaults(func=cacheMode.commit, do='cache-mode')

    site_cache_rule_parser = cache_subparsers.add_parser('cache-rule', help='Use this operation to edit basic '
                                                                            'site caching settings.',
        usage='incap [options] site cache-rule [options] site_id')
    site_cache_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_cache_rule_parser.add_argument('--always_cache_resource_url', default='',
        help="Comma separated list of always cache resources url")
    site_cache_rule_parser.add_argument('--always_cache_resource_pattern', default='',
        help="Comma separated list of always cache resources pattern. "
             "One of: contains | equals | prefix | suffix | not_equals | not_contains "
             "| not_prefix | not_suffix")
    site_cache_rule_parser.add_argument('--always_cache_resource_duration', default='',
        help="Duration that resources will be in cache, pass number followed by "
             "'_' and one of: hr | min | sec | days | weeks. "
             "Either provide a comma separated list of duration expressions, "
             "matching the number of always cache rules, "
             "or a single duration expression to be used for all always cache rules.")
    site_cache_rule_parser.add_argument('--never_cache_resource_url', default='',
        help="Comma separated list of never cache resources url.")
    site_cache_rule_parser.add_argument('--never_cache_resource_pattern', default='',
        help="Comma separated list of never cache resources pattern. "
             "One of: contains | equals | prefix | suffix | not_equals "
             "| not_contains | not_prefix | not_suffix")
    site_cache_rule_parser.add_argument('--cache_headers', default='',
        help="Comma separated list of cached headers.")
    site_cache_rule_parser.add_argument('--clear_always_cache_rules', default='',
        help="An optional boolean parameter. If set to 'true', "
             "the site's always cache rules will be cleared.")
    site_cache_rule_parser.add_argument('--clear_never_cache_rules', default='',
        help="An optional boolean parameter. If set to 'true', "
             "the site's never cache rules will be cleared.")
    site_cache_rule_parser.add_argument('--clear_cache_headers_rules', default='',
        help="An optional boolean parameter. If set to 'true', "
             "the site's cache header rules will be cleared.")
    site_cache_rule_parser.set_defaults(func=u_cacherule)

    site_advanced_cache_parser = cache_subparsers.add_parser('advanced-cache',
        help='Use this operation to modify advanced caching settings.',
        usage='incap [options] site advanced-cache param value '
              'site_id')
    site_advanced_cache_parser.add_argument('param', help="Name of configuration parameter to set. See table below.")
    site_advanced_cache_parser.add_argument('value', help="According to the param value. See table below.")
    site_advanced_cache_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_advanced_cache_parser.set_defaults(func=u_advanced)

    site_get_cache_settings_parser = cache_subparsers.add_parser('get-cache-settings', help='Get cache settings',
        usage='incap [options] site get-cache-settings [options] '
              'site_id')
    site_get_cache_settings_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_get_cache_settings_parser.add_argument('--sections',
        help='The sections of configurations to get, separated by '
             'comma. If not passed, all sections will be returned. '
             'Available values : mode, key, response, ttl, '
             'client_side')
    site_get_cache_settings_parser.set_defaults(func=CacheSettings.read)

    site_change_cache_settings_parser = cache_subparsers.add_parser('change-cache-settings',
        help='Change cache settings',
        usage='incap [options] site change-cache-settings ['
              'options] site_id')
    site_change_cache_settings_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_change_cache_settings_parser.add_argument('json', help='The section of configurations to change. Available '
                                                                'values : mode, key, response, ttl, client_side')
    site_change_cache_settings_parser.set_defaults(func=CacheSettings.override)

    site_delete_cache_settings_parser = cache_subparsers.add_parser('delete-cache-settings',
        help='Restore default cache settings',
        usage='incap [options] site delete-cache-settings ['
              'options] site_id')
    site_delete_cache_settings_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_delete_cache_settings_parser.set_defaults(func=CacheSettings.delete)

    site_create_cache_settings_rule_parser = cache_subparsers.add_parser('create-cache-settings-rule',
        help='Create cache rule',
        usage='incap [options] site '
              'create-cache-settings-rule site_id')
    site_create_cache_settings_rule_parser.add_argument('name', help='Rule name')
    site_create_cache_settings_rule_parser.add_argument('action', help='Define the action you want to take for every '
                                                                       'request that matches the '
                                                                       'rule.HTTP_CACHE_MAKE_STATIC, '
                                                                       'HTTP_CACHE_CLIENT_CACHE_CTL, '
                                                                       'HTTP_CACHE_FORCE_UNCACHEABLE, HTTP_CACHE_ADD_TAG, '
                                                                       'HTTP_CACHE_DIFFERENTIATE_SSL, '
                                                                       'HTTP_CACHE_DIFFERENTIATE_BY_HEADER, '
                                                                       'HTTP_CACHE_DIFFERENTIATE_BY_COOKIE, '
                                                                       'HTTP_CACHE_DIFFERENTIATE_BY_GEO, '
                                                                       'HTTP_CACHE_IGNORE_PARAMS, '
                                                                       'HTTP_CACHE_ENRICH_CACHE_KEY, '
                                                                       'HTTP_CACHE_FORCE_VALIDATION, '
                                                                       'HTTP_CACHE_IGNORE_AUTH_HEADER')
    site_create_cache_settings_rule_parser.add_argument('enabled', help='If the rule is enabled.')
    site_create_cache_settings_rule_parser.add_argument('filter', help='The filter defines the conditions that trigger '
                                                                       'the rule action, if left empty, the rule is '
                                                                       'always run.')
    site_create_cache_settings_rule_parser.add_argument('--ttl', help='TTL in seconds. Relevant for '
                                                                      'HTTP_CACHE_MAKE_STATIC and '
                                                                      'HTTP_CACHE_CLIENT_CACHE_CTL actions.')
    site_create_cache_settings_rule_parser.add_argument('--ignored_params', help='Parameters to ignore. Relevant for '
                                                                                 'HTTP_CACHE_IGNORE_PARAMS action. An '
                                                                                 "array containing '*' means all "
                                                                                 'parameters are '
                                                                                 'ignored.')
    site_create_cache_settings_rule_parser.add_argument('--text',
        help='Tag name if action is HTTP_CACHE_ADD_TAG action, '
             'text to be added to the cache key as suffix if '
             'action is HTTP_CACHE_ENRICH_CACHE_KEY.')
    site_create_cache_settings_rule_parser.add_argument('--differentiate_by_value', help='Value to differentiate '
                                                                                         'resources by. Relevant for '
                                                                                         'HTTP_CACHE_DIFFERENTIATE_BY_HEADER, HTTP_CACHE_DIFFERENTIATE_BY_COOKIE and HTTP_CACHE_DIFFERENTIATE_BY_GEO actions')
    site_create_cache_settings_rule_parser.add_argument('--rule', help='JSON string that contains rule.')
    site_create_cache_settings_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_create_cache_settings_rule_parser.set_defaults(func=CacheRule.create)

    site_update_cache_settings_rule_parser = cache_subparsers.add_parser('update-cache-settings-rule',
        help='Update cache rule',
        usage='incap [options] site '
              'update-cache-settings-rule site_id rule_id')
    site_update_cache_settings_rule_parser.add_argument('--name', help='Rule name')
    site_update_cache_settings_rule_parser.add_argument('--action', help='Define the action you want to take for every '
                                                                         'request that matches the '
                                                                         'rule.HTTP_CACHE_MAKE_STATIC, '
                                                                         'HTTP_CACHE_CLIENT_CACHE_CTL, '
                                                                         'HTTP_CACHE_FORCE_UNCACHEABLE, HTTP_CACHE_ADD_TAG, '
                                                                         'HTTP_CACHE_DIFFERENTIATE_SSL, '
                                                                         'HTTP_CACHE_DIFFERENTIATE_BY_HEADER, '
                                                                         'HTTP_CACHE_DIFFERENTIATE_BY_COOKIE, '
                                                                         'HTTP_CACHE_DIFFERENTIATE_BY_GEO, '
                                                                         'HTTP_CACHE_IGNORE_PARAMS, '
                                                                         'HTTP_CACHE_ENRICH_CACHE_KEY, '
                                                                         'HTTP_CACHE_FORCE_VALIDATION, '
                                                                         'HTTP_CACHE_IGNORE_AUTH_HEADER')
    site_update_cache_settings_rule_parser.add_argument('--enabled', help='If the rule is enabled.')
    site_update_cache_settings_rule_parser.add_argument('--filter',
        help='The filter defines the conditions that trigger '
             'the rule action, if left empty, the rule is '
             'always run.')
    site_update_cache_settings_rule_parser.add_argument('--ttl', help='TTL in seconds. Relevant for '
                                                                      'HTTP_CACHE_MAKE_STATIC and '
                                                                      'HTTP_CACHE_CLIENT_CACHE_CTL actions.')
    site_update_cache_settings_rule_parser.add_argument('--ignored_params', help='Parameters to ignore. Relevant for '
                                                                                 'HTTP_CACHE_IGNORE_PARAMS action. An '
                                                                                 "array containing '*' means all "
                                                                                 'parameters are '
                                                                                 'ignored.')
    site_update_cache_settings_rule_parser.add_argument('--text',
        help='Tag name if action is HTTP_CACHE_ADD_TAG action, '
             'text to be added to the cache key as suffix if '
             'action is HTTP_CACHE_ENRICH_CACHE_KEY.')
    site_update_cache_settings_rule_parser.add_argument('--differentiate_by_value', help='Value to differentiate '
                                                                                         'resources by. Relevant for '
                                                                                         'HTTP_CACHE_DIFFERENTIATE_BY_HEADER, HTTP_CACHE_DIFFERENTIATE_BY_COOKIE and HTTP_CACHE_DIFFERENTIATE_BY_GEO actions')
    site_update_cache_settings_rule_parser.add_argument('--json', help='JSON string that contains rule.')
    site_update_cache_settings_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_update_cache_settings_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to get.')
    site_update_cache_settings_rule_parser.set_defaults(func=CacheRule.update)

    site_get_cache_settings_rule_parser = cache_subparsers.add_parser('get-cache-settings-rule',
        help='Get cache rule - '
             'must contain valid '
             'rule id',
        usage='incap [options] site get-cache-settings ['
              'options] site_id')
    site_get_cache_settings_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_get_cache_settings_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to get.')
    site_get_cache_settings_rule_parser.set_defaults(func=CacheRule.read)

    site_list_cache_settings_rule_parser = cache_subparsers.add_parser('list-cache-settings-rule',
        help='List cache rule - '
             'must contain valid '
             'rule id',
        usage='incap [options] site list-cache-settings-rule '
              'site_id')
    site_list_cache_settings_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_list_cache_settings_rule_parser.set_defaults(func=CacheRule.list)

    site_delete_cache_settings_rule_parser = cache_subparsers.add_parser('delete-cache-settings-rule',
        help='Delete cache '
             'rule - must '
             'contain valid '
             'rule id',
        usage='incap [options] site '
              'delete-cache-settings-rule '
              'site_id rule_id')
    site_delete_cache_settings_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_delete_cache_settings_rule_parser.add_argument('rule_id', help='Numeric identifier of the rule to get.')
    site_delete_cache_settings_rule_parser.set_defaults(func=CacheRule.delete)

    site_get_delivery_settings_parser = cache_subparsers.add_parser('get-delivery-settings',
        help='Get delivery settings',
        usage='incap [options] site get-delivery-settings'
              ' [options] site_id')
    site_get_delivery_settings_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_get_delivery_settings_parser.add_argument('--sections',
        help='The sections of configurations to get, separated '
             'by comma. If not passed, all sections will be '
             'returned. Available values : compression, '
             'image_compression, network, '
             'redirection, custom_error_page')
    site_get_delivery_settings_parser.set_defaults(func=DeliverySettings.read)

    site_update_delivery_settings_parser = cache_subparsers.add_parser('update-delivery-settings',
        help='Get delivery settings',
        usage='incap [options] site '
              'update-delivery-settings site_id')
    site_update_delivery_settings_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
    site_update_delivery_settings_parser.add_argument('json', help='The JSON delivery settings to use.')
    site_update_delivery_settings_parser.set_defaults(func=DeliverySettings.override)
