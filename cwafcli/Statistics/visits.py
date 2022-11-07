import logging
from operator import itemgetter
from ..Utils.executeRest import execute
from ..Utils.print_ifp_stats import PrintTable
from ..Utils.table_formatter import TableFormatter


class Event:
    def __init__(self, data):
        self.accountId = data["accountId"]
        self.eventTime = data["eventTime"]
        self.eventType = data["eventType"]
        self.itemType = data["itemType"]
        self.eventTarget = data["eventTarget"]

    @staticmethod
    def commit(args):
        param = vars(args)
        action = param['do']
        logging.basicConfig(format='%(levelname)s - %(message)s',  level=getattr(logging, args.log.upper()))
        resturl = 'https://my.incapsula.com/api/v1/infra/{}'.format(action)

        if action == "events":
            Event.print_events(execute(resturl, param)["events"])
        elif action == "stats":
            Event.print_stats(execute(resturl, param)["stats"][0]["payload"])

    @staticmethod
    def print_events(events: list):
        if len(events) > 0:
            newlist = sorted(events, key=itemgetter('eventTime'))
            format_site = TableFormatter(headers=['accountId', 'eventTime', 'eventType', 'itemType', 'eventTarget'], data=newlist)
            PrintTable(label='Events', data=format_site).print_all()
        else:
            logging.info("There are no events at this time.")

    @staticmethod
    def print_stats(events: list):
        newlist = sorted(events, key=itemgetter('startTime'))
        format_site = TableFormatter(headers=['metric', 'ipPrefix', 'pop', 'trafficType', 'ipPrefixType', 'traffic', 'startTime', 'data'], data=newlist)
        PrintTable(label='Stats', data=format_site).print_all()
