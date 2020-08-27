import logging
from operator import itemgetter
from ..Utils.executeRest import execute
from ..Utils.print_table import PrintTable
from ..Utils.table_formatter import TableFormatter


class Stats:
    def __init__(self, data):
        self.accountId = data["accountId"]
        self.eventTime = data["eventTime"]
        self.eventType = data["eventType"]
        self.itemType = data["itemType"]
        self.eventTarget = data["eventTarget"]

    @staticmethod
    def commit(args):
        param = vars(args)
        # action = param['do']
        # print('{} site data centers.'.format(str.capitalize(action)))
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/stats/v1'


        result = execute(resturl, param)
        Stats.format_data(result)
        exit(0)

    # @staticmethod
    # def print_events(events: list):
    #     if len(events) > 0:
    #         newlist = sorted(events, key=itemgetter('eventTime'))
    #         format_site = TableFormatter(headers=['accountId', 'eventTime', 'eventType', 'itemType', 'eventTarget'], data=newlist)
    #         PrintTable(label='Events', data=format_site).print_all()
    #     else:
    #         logging.info("There are no events at this time.")

    @staticmethod
    def print_stats(events: list):
        newlist = sorted(events, key=itemgetter('startTime'))
        format_site = TableFormatter(headers=['metric', 'ipPrefix', 'pop', 'trafficType', 'ipPrefixType', 'traffic', 'startTime', 'data'], data=newlist)
        PrintTable(label='Stats', data=format_site.headers).print_all()

    @staticmethod
    def format_data(data):
        ignore_list = ["res", "res_message", "debug_info"]
        allow_list = ["visits_timeseries", "hits_timeseries", "bandwidth_timeseries", "caching_timeseries"]
        stat = {}
        formated_stats = []
        for k, v in data.items():
            if k not in ignore_list and k in allow_list:
                for dt in data[k]:
                    type = dt["name"]
                    for stat_time in dt["data"]:
                        import time
                        stat.update(timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_time[0] / 1000.0)))
                        stat.update(value=stat_time[1])
                        formated_stats.append(stat.copy())
                    logging.info(sorted(formated_stats, key=itemgetter("timestamp")))
                # for dt in data[k]:
                #     stat["name"] = dt["name"]
                #     for stat_time in dt["data"]:
                #         import time
                #         stat.update(timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_time[0] / 1000.0)))
                #         stat.update(value=stat_time[1])
                #         formated_stats.append(stat.copy())
                #     logging.info(sorted(formated_stats, key=itemgetter("timestamp")))
        format_site = TableFormatter(headers=['name', 'timestamp', 'value'], data=sorted(formated_stats, key=itemgetter("timestamp")))
        PrintTable(label='Stats', data=format_site.headers).print_all()