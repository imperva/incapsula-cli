from ..Utils.executeRest import execute


class Rules:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules".format(**param),
                       param, "POST", param)

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                       param, "GET", param)

    @staticmethod
    def list(args):
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v1/sites/incapRules/list", param, body=param)

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
