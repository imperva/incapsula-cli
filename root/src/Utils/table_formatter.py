class TableFormatter:
    def __init__(self, headers: list, data: list):
        self.headers = []
        self.req_headers = headers
        self.width = []
        self.data = data
        self.set_headers()
        self.set_width()
        self.format_headers()

    def print_data(self):
        print('Data:{}'.format(self.data))

    def set_headers(self):
        _items = []
        for data in self.data:
            header = []
            for req_headers in self.req_headers:
                header.append([req_headers, data.get(req_headers)])
            _items.append(header)
        self.headers = _items

    def set_width(self):
        for header in self.headers:
            for v in header:
                if len(self.width) != len(header):
                    self.width.insert(header.index(v), TableFormatter._the_larger(len(v[0]), len(str(v[1]))))
                elif len(v[0]) > self.width[header.index(v)] or len(str(v[1])) > self.width[header.index(v)]:
                    self.width[header.index(v)] = TableFormatter._the_larger(len(v[0]), len(str(v[1])))

    def format_headers(self):
        for header in self.headers:
            for v in header:
                v.append(self.width[header.index(v)])

    @staticmethod
    def _the_larger(header, value):
        if header > value:
            return header
        else:
            return value
