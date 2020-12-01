from ..Utils.executeRest import execute


class Cache:
    def __init__(self, data):
        self.acceleration_level = data.get('acceleration_level') or None
        self.aggressive_compression = data.get('aggressive_compression') or None
        self.async_validation = data.get('async_validation') or bool
        self.cache300x = data.get('cache300x' or bool)
        self.cache_headers = data.get('cache_headers') or []
        self.comply_no_cache = data.get('comply_no_cache') or bool
        self.comply_vary = data.get('comply_vary') or bool
        self.compress_jepg = data.get('compress_jepg') or bool
        self.compress_jpeg = data.get('compress_jpeg') or bool
        self.compress_png = data.get('compress_png') or bool
        self.disable_client_side_caching = data.get('disable_client_side_caching') or bool
        self.minify_css = data.get('minify_css') or bool
        self.minify_javascript = data.get('minify_javascript') or bool
        self.minify_static_html = data.get('minify_static_html') or bool
        self.on_the_fly_compression = data.get('on_the_fly_compression') or bool
        self.perfer_last_modified = data.get('perfer_last_modified') or bool
        self.prefer_last_modified = data.get('prefer_last_modified') or bool
        self.progressive_image_rendering = data.get('progressive_image_rendering') or bool
        self.tcp_pre_pooling = data.get('tcp_pre_pooling') or bool
        self.use_shortest_caching = data.get('use_shortest_caching') or bool
        self.advanced_caching_rules = data.get('advanced_caching_rules') or {}
        self.always_cache_resources = self.advanced_caching_rules.get('always_cache_resources') or []
        self.always_cache_resource_url = self._always_cache_resource_url(self.always_cache_resources) or ''
        self.always_cache_resource_pattern = self._always_cache_resource_pattern(self.always_cache_resources) or ''
        self.always_cache_resource_duration = self._always_cache_resource_duration(self.always_cache_resources) or ''
        self.never_cache_resources = self.advanced_caching_rules.get('never_cache_resources') or []
        self.never_cache_resource_url = self._never_cache_resource_url(self.never_cache_resources) or ''
        self.never_cache_resource_pattern = self._never_cache_resource_pattern(self.never_cache_resources) or ''
        self.clear_always_cache_rules = self._clear_always_cache_rules
        self.clear_never_cache_rules = self._clear_never_cache_rules
        self.clear_cache_headers_rules = self._clear_cache_headers_rules

    @staticmethod
    def _always_cache_resource_url(data):
        value = None
        for resource in data:
            value = resource.get('url') or ''
        return value or ''

    @staticmethod
    def _always_cache_resource_pattern(data):
        value = None
        for resource in data:
            value = resource.get('pattern') or ''
        return value or ''

    @staticmethod
    def _always_cache_resource_duration(data):
        value = None
        for resource in data:
            value = str(resource.get('ttl') or '')
            value += '_'
            value += str(resource.get('ttlUnits') or '')
        return value or ''

    @staticmethod
    def _never_cache_resource_url(data):
        value = None
        for resource in data:
            value = resource.get('url') or ''
        return value or ''

    @staticmethod
    def _never_cache_resource_pattern(data):
        value = None
        for resource in data:
            value = resource.get('pattern') or ''
        return value or ''

    @staticmethod
    def _clear_always_cache_rules():
        return False

    @staticmethod
    def _clear_never_cache_rules():
        return False

    @staticmethod
    def _clear_cache_headers_rules():
        return False

    def _caching_rules(self):
        return {
            "always_cache_resource_url": self.always_cache_resource_url,
            "always_cache_resource_pattern": self.always_cache_resource_pattern,
            "never_cache_resource_url": self.never_cache_resource_url,
            "never_cache_resource_pattern": self.never_cache_resource_pattern,
            "cache_headers": self.cache_headers,
            "clear_always_cache_rules": self.clear_always_cache_rules,
            "clear_never_cache_rules": self.clear_never_cache_rules,
            "clear_cache_headers_rules": self.clear_cache_headers_rules
        }


class CacheSettings:
    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache".format(**param),
                       param, "GET", param)

    @staticmethod
    def override(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache".format(**param),
                       param, "PUT", param["json"])

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = CacheSettings.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache".format(**source),
                       source, "PUT", source)


class CacheRule:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules".format(**param),
                       param, "POST", param)

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules/{rule_id}".format(**param),
                       param, "GET", param)

    @staticmethod
    def list(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules".format(**param),
                       param, "GET")

    @staticmethod
    def update(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules/{rule_id}".format(**param),
                       param, "PUT", param)

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules/{rule_id}".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = CacheRule.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/cache/rules".format(**source),
                       source, "POST", source)


class DeliverySettings:
    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/delivery".format(**param),
                       param, "GET", param)

    @staticmethod
    def override(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/delivery".format(**param),
                       param, "PUT", param["json"])

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/delivery".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = DeliverySettings.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/settings/delivery".format(**source),
                       source, "PUT", source)