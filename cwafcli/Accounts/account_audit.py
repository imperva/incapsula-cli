import time


class Audit:
    def __init__(self, data):
        self.createdAt = time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(int(data.get('createdAt'))/1000.0)) or ''
        self.account_id = data.get('account_id') or ''
        self.user_id = data.get('user_id') or ''
        self.type_key = data.get('type_key') or ''
        self.type_description = data.get('type_description') or ''
        self.context = data.get('context') or ''
        self.response_message = data.get('res_message') or ''
        self.site_id = data.get('site_id') or ''
        self.changes = data.get('changes') or ''

    def log(self):
        return '-------------------------------------------------------------------------\n' \
               'Audit Details:\nTime: %s\nAccount ID: %s\nUser ID: %s\nDescription: %s' \
               '\nContext: %s\nChanges: %s' % (self.createdAt, self.account_id, self.user_id,
                                               self.type_description, self.context, self.changes)
