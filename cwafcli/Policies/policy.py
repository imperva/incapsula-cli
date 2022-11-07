import json

from ..Utils.executeRest import execute


class Policy:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/policies".format(**param),
                       param, "POST", param["json"])

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/policies/{policy_id}?extended={extended}".format(**param),
                       param, "GET", param)

    @staticmethod
    def list(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/policies?extended={extended}".format(**param), param, "GET")

    @staticmethod
    def update(args):
        param = vars(args)
        json_str = json.loads(param["json"])
        try:
            del json_str["lastModifiedBy"]
            del json_str["lastModified"]
        except:
            pass
        return execute("https://api.imperva.com/policies/v2/policies/{policy_id}".format(**param),
                       param, "POST", json_str)

    @staticmethod
    def override(args):
        param = vars(args)
        json_str = json.loads(param["json"])
        print("What type: {}".format(type(json_str)))
        try:
            del json_str["lastModifiedBy"]
            del json_str["lastModified"]
        except:
            pass
        json_str = json.dumps(json_str)
        return execute("https://api.imperva.com/policies/v2/policies/{policy_id}".format(**param),
                       param, "PUT", json_str)

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/policies/{policy_id}".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = Policy.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://api.imperva.com/policies/v2/policies".format(**source),
                       source, "POST", source)


class AssetAssociation:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/assets/{asset_type}/{asset_id}/policies/{policy_id}".format(**param),
                       param, "POST", param)

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/assets/policies/{policy_id}".format(**param),
                       param, "GET")

    @staticmethod
    def list(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/assets/{asset_type}/{asset_id}/policies", param, "GET")

    @staticmethod
    def override(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/assets/{asset_type}/{asset_id}/policies/{policy_id}".format(**param),
                       param, "PUT", param)

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://api.imperva.com/policies/v2/assets/{asset_type}/{asset_id}/policies/{policy_id}".format(**param),
                       param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = Policy.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://api.imperva.com/policies/v2/policies".format(**source),
                       source, "POST", source)