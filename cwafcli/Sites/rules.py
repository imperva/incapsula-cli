from ..Utils.executeRest import execute
import logging


class Rules:
    @staticmethod
    def create(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        return execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules".format(**param),
                       param, "POST", param)

    @staticmethod
    def read(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                param, "GET", param)

    @staticmethod
    def update(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/{rule_id}".format(**param),
                param, "POST", param)

    @staticmethod
    def override(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        execute("https://my.imperva.com/api/prov/v2/sites/{site_id}/rules/{rule_id}".format(**param),
                param, "PUT", param)

    @staticmethod
    def delete(args):
        logging.basicConfig(format='%(levelname)s - %(message)s', level=getattr(logging, args.log.upper()))
        param = vars(args)
        execute("https://my.imperva.com/api/prov/v2/sites/{siteId}/rules/{ruleId}".format(**param),
                param, "DELETE", param)
