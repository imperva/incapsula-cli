import time
from ..Sites.site import Site
from ..Utils.executeRest import execute
from ..Utils.incapError import IncapError
import logging
from ..Utils.print_table import PrintTable
from ..Utils.table_formatter import TableFormatter


def r_sites(args):
    output = 'Getting site list.'
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = vars(args)

    result = read(param)
    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        format_site = TableFormatter(headers=['domain', 'status', 'site_id', 'log_level'], data=result['sites'])
        PrintTable(label='Sites', data=format_site.headers).print_all()


def create_filename(filename, site):
    site = Site(site)
    if filename == "{site_id}_{domain}":
        return "{}_{}".format(site.site_id, site.domain)
    elif filename == "{domain}_{site_id}":
        return "{}_{}".format(site.domain, site.site_id)
    elif filename == "{domain}_{date}":
        return "{}_{}".format(site.domain, time.strftime("%Y%m%d-%H%M%S"))
    elif filename == "{site_id}_{date}":
        return "{}_{}".format(site.site_id, time.strftime("%Y%m%d-%H%M%S"))
    elif filename == "{domain}":
        return "{}".format(site.domain)
    elif filename == "{site_id}":
        return "{}".format(site.site_id)
    elif filename.startswith("{site_id}_{domain}") and not filename.endswith("_{date}"):
        return "{}_{}_{}".format(site.site_id, site.domain,
                                 filename.replace("{site_id}_{domain}", '').replace('.', '_'))
    else:
        return "{}_{}_{}".format(site.site_id, site.domain, time.strftime("%Y%m%d-%H%M%S"))


def read(params):
    resturl = 'sites/list'
    if params:
        if "account_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No account_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
