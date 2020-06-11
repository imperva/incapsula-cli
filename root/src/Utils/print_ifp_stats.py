from Utils.table_formatter import TableFormatter


class PrintTable:
    def __init__(self, label, data: TableFormatter):
        self.data = data
        self.label = label
        self.bucket = []
        self.five_95_bucket = []

    def print_all(self):
        self.print_label()
        self.print_headers()
        self.print_values()

    def print_label(self):
        print('#' * len(self.label) + '\n' + self.label + '\n' + '#' * len(self.label))

    def print_headers(self):
        header = '|'
        for headers in self.data.req_headers:
            header += "{0:^{1}}|".format(headers.capitalize(), 18)
        print('~' * len(header) + '\n' + header + '\n' + '~' * len(header))

    def print_values(self):
        p = None
        value = '|'
        for data in self.data.data:
            if 'pop' not in data and 'trafficType' not in data and 'ipPrefix' not in data:
                if data['metric'] == 'bw':#or data['metric'] == 'pps':
                    self.makeBucket(data['data'], data['interval'])
                    print(PrintTable.nintyFifth(data['data'], 95))
                    for header in self.data.req_headers:
                        if header in data:
                            if type(data[header]) == list:
                                if data["metric"] == "bw":
                                    value += "{0:^{1}}|".format(PrintTable.avgBandwidth(data[header]), 18)
                                else:
                                    value += "{0:^{1}}|".format(sum(data[header]), 18)
                            elif header == "startTime":
                                value += "{0:^{1}}|".format(PrintTable.convertTime(data.get(header)), 18)
                            else:
                                value += "{0:^{1}}|".format(data.get(header), 18)
                        else:
                            value += "{0:^{1}}|".format("null", 18)
                    print('-' * len(value) + '\n' + value + '\n' + '-' * len(value))
                    value = '|'
                    if p: p.print_all()

    def makeBucket(self, lst, interval):

        divider = int(300000 / interval)
        end = divider
        start = 0
        print("list length: {}".format(len(lst)))
        while start < len(lst):
            print("Grabbing Start={}, End={}".format(start, end))
            self.five_95_bucket.append(PrintTable.nintyFifth(lst[start:end], 95))
            start += divider
            end += divider

        # print(self.bucket)
        # print(PrintTable.nintyFifth(self.bucket, 95))
        print(self.five_95_bucket)

    @staticmethod
    def nintyFifth(lst, percentile):
        import math
        size = len(lst)
        return sorted(lst)[int(math.ceil((size * percentile) / 100)) - 1]

        gbps = 1_000_000_000
        mbps = 1_000_000
        kbps = 1_000

        if nintyfive > gbps:
            return "{} Gbps".format(round((nintyfive / gbps), 2)), int(nintyfive / gbps)
        elif nintyfive > mbps:
            return "{} Mbps".format(round((nintyfive / mbps), 2))
        elif nintyfive > kbps:
            return "{} Kbps".format(round((nintyfive / kbps), 2))
        else:
            return "{} bps".format(nintyfive)

        # print("{}% = {}".format(percentile, nintyfive))
    #     print("{}% = {}".format(percentile, numpy.percentile(lst, percentile) / 1_000_000_000))

    @staticmethod
    def avgBandwidth(lst):
        return (sum(lst) / len(lst)) / 1024

    @staticmethod
    def convertTime(epoch):
        import time
        return time.strftime("%b %d %H:%M:%S", time.gmtime(epoch / 1000))
