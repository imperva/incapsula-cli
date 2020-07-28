from ..Utils.table_formatter import TableFormatter


class PrintTable:
    def __init__(self, label, data: list):
        self.data = data
        self.label = label

    def print_all(self):
        self.print_label()
        self.print_headers()
        self.print_values()

    def print_label(self):
        print('#' * len(self.label) + '\n' + self.label + '\n' + '#' * len(self.label))

    def print_headers(self):
        header = '|'
        for headers in self.data[0]:
            if type(headers[1]) is not list:
                header += "{0:^{1}}|".format(headers[0].capitalize(), str(headers[2]))
        print('~' * len(header) + '\n' + header + '\n' + '~' * len(header))

    def print_values(self):
        p = None
        value = '|'
        for data in self.data:
            for values in data:
                if type(values[1]) is list:
                    headers = list(values[1][0].keys())
                    format_site = TableFormatter(headers=headers, data=values[1])
                    p = PrintTable(label=values[0].capitalize(), data=format_site.headers)
                else:
                    try:
                        value += "{0:^{1}}|".format(values[1], str(values[2]))
                    except:
                        pass
            print('-' * len(value) + '\n' + value + '\n' + '-' * len(value))
            value = '|'
            if p: p.print_all()

