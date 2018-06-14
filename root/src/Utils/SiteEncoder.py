from json import JSONEncoder


class SiteEncoder(JSONEncoder):
    def default(self, o):
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}