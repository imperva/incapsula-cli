from ..Utils.table_formatter import TableFormatter


class PrintTable:
    def __init__(self, label, data: TableFormatter):
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
        for headers in self.data.req_headers:
            header += "{0:^{1}}|".format(headers.capitalize(), 18)
        print('~' * len(header) + '\n' + header + '\n' + '~' * len(header))

    def print_values(self):
        p = None
        value = '|'
        for data in self.data.data:
            for header in self.data.req_headers:
                if header in data:
                    if type(data[header]) == list:
                        value += "{0:^{1}}|".format(data[header][0], 18)
                    else:
                        value += "{0:^{1}}|".format(data.get(header), 18)
                else:
                    value += "{0:^{1}}|".format("null", 18)
            print('-' * len(value) + '\n' + value + '\n' + '-' * len(value))
            value = '|'
            if p: p.print_all()

