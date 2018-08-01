import logging


class IncapError:
    def __init__(self, err):
        self.data = err
        self.res = err.get('res')
        self.res_message = err.get('res_message')
        self.debug_info = err.get('debug_info')

    def log(self):
        logging.error('Result Code: %s - Result Message: %s' % (
            str(self.data.get('res')), self.data.get('res_message')))
        for k, v in self.data['debug_info'].items():
            logging.error('%s - %s' % (str.upper(k), str.replace(v, '<br/>', '\n')))

    def get_res(self):
        return self.res

    def get_res_message(self):
        return self.res_message

    def get_debug_info(self):
        return self.debug_info
