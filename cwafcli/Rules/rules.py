from ..Utils.executeRest import execute


class Rules:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules".format(**param),
                       param, "POST", param["json"])

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                       param, "GET", param)

    @staticmethod
    def list(args):
        param = vars(args)
        response = execute("https://my.imperva.com/api/prov/v1/sites/incapRules/list", param, body=param)
        if args.output == "friendly" and "custom_error_response_rules" in response:
            if "RewriteResponse" in response["custom_error_response_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'error_type', 'error_response_format'], data=response['custom_error_response_rules']['RewriteResponse'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Custom Error Response Rules', data=format_site.headers).print_all()
        if args.output == "friendly" and "delivery_rules" in response:
            if "Rewrite" in response["delivery_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'action', 'rewrite_name', 'from', 'to'],
                    data=response['delivery_rules']['Rewrite'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Rewrite', data=format_site.headers).print_all()
            if "Redirect" in response["delivery_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'from', 'to', 'response_code'],
                    data=response['delivery_rules']['Redirect'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Redirect', data=format_site.headers).print_all()
            if "RewriteResponse" in response["delivery_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'action'], data=response['delivery_rules']['RewriteResponse'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Rewrite Response', data=format_site.headers).print_all()
            if "SimplifiedRedirect" in response["delivery_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'from', 'to', 'response_code'], data=response['delivery_rules']['SimplifiedRedirect'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Simplified Redirect', data=format_site.headers).print_all()
        if args.output == "friendly" and "incap_rules" in response:
            if "All" in response["incap_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'action'], data=response['incap_rules']['All'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Security Rules', data=format_site.headers).print_all()
            if "WafOverride" in response["incap_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'enabled'], data=response['incap_rules']['WafOverride'])
                from cwafcli.Utils.print_table import PrintTable
                return PrintTable(label='WAF Override', data=format_site.headers).print_all()
        if args.output == "friendly" and "rate_rules" in response:
            if "Rates" in response["rate_rules"]:
                from cwafcli.Utils.table_formatter import TableFormatter
                format_site = TableFormatter(headers=['name', 'id', 'filter', 'context', 'interval', 'context', 'enabled'], data=response['rate_rules']['Rates'])
                from cwafcli.Utils.print_table import PrintTable
                PrintTable(label='Rates', data=format_site.headers).print_all()
        else:
            return response

    @staticmethod
    def update(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                       param, "POST", param)

    @staticmethod
    def override(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                       param, "PUT", param)

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = Rules.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules".format(**source),
                       source, "POST", source)
