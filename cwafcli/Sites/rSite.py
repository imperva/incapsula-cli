from ..Utils.print_table import PrintTable
from ..Utils.table_formatter import TableFormatter
from ..Utils.executeRest import execute
from ..Sites.site import Site
from ..Utils.incapError import IncapError
import logging


def r_site(args):
    output = 'Get site status for ID = {0}'. format(args.site_id)
    logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
    print(output)
    param = vars(args)

    result = read(param)

    if int(result.get('res')) != 0:
        err = IncapError(result)
        err.log()
        return err
    else:
        #
        # format_site = TableFormatter(headers=['domain', 'status', 'site_id', 'account_id',
        #                                       'acceleration_level', 'site_creation_date', 'active',
        #                                       'support_all_tls_versions', 'extended_ddos', 'log_level']
        #                              , data=[result])
        # PrintTable(label='Sites', data=format_site.headers).print_all()
        site = Site(result)
        site.log()
        return site


def read(params):
    resturl = 'sites/status'
    if params:
        if "site_id" in params:
            return execute(resturl, params)
        else:
            logging.warning("No site_id parameter has been passed in for %s." % __name__)
    else:
        logging.error('No parameters where passed in.')
