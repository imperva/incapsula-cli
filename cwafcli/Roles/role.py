import json

from ..Utils.executeRest import execute


class Abilities:
    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/abilities/accounts/{account_id}".format(**param),
            param, "GET")


class Role:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/roles".format(**param),
            param, "POST", param["json"])

    @staticmethod
    def read(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/roles/{role_id}".format(**param),
            param, "GET", param)

    @staticmethod
    def list(args):
        param = vars(args)
        query = "accountId={account_id}".format(**param)
        if param["userEmail"]:
            query += "&userEmail={userEmail}".format(**param)
        if param["roleName"]:
            query += "&roleName={roleName}".format(**param)

        return execute("https://api.imperva.com/user-management/v1/roles?{}".format(query), param, "GET")

    @staticmethod
    def update(args):
        param = vars(args)
        json_str = json.loads(param["json"])
        try:
            del json_str["lastModifiedBy"]
            del json_str["lastModified"]
        except:
            pass
        return execute("https://api.imperva.com/user-management/v1/roles/{role_id}".format(**param),
            param, "POST", json_str)

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/roles/{role_id}".format(**param),
            param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = Role.read(args)
        source["roles_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://api.imperva.com/user-management/v1/roles".format(**source),
            source, "POST", source)


class Assignment:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/assignments",
            param, "POST", param["json"])

    @staticmethod
    def read(args):
        param = vars(args)
        return execute(
            "https://api.imperva.com/user-management/v1/assignments?userEmail={userEmail}&accountId={account_id}".format(
                **param),
            param, "GET")

    @staticmethod
    def duplicate(args):
        source = Assignment.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://api.imperva.com/user-management/v1/policies".format(**source),
            source, "POST", source)


class User:
    @staticmethod
    def create(args):
        param = vars(args)
        return execute("https://api.imperva.com/user-management/v1/users",
            param, "POST", param["json"])

    @staticmethod
    def read(args):
        param = vars(args)
        return execute(
            "https://api.imperva.com/user-management/v1/users?userEmail={userEmail}&account_id={account_id}".format(
                **param),
            param, "GET")

    @staticmethod
    def delete(args):
        param = vars(args)
        return execute(
            "https://api.imperva.com/user-management/v1/users?userEmail={userEmail}&accountId={account_id}".format(
                **param),
            param, "DELETE", param)

    @staticmethod
    def duplicate(args):
        source = User.read(args)
        source["site_id"] = args.dup_site_id
        source["profile"] = args.profile
        return execute("https://api.imperva.com/user-management/v1/users".format(**source),
            source, "POST", source)
