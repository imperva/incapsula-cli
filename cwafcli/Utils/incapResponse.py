import logging


class IncapResponse:
    def __init__(self, data):
        self.data = data
        self.res = data.get('res')
        self.res_message = data.get('res_message')
        self.debug_info = data.get('debug_info')
        self.rule_id = data.get('rule_id')

    def log(self):
        logging.debug('Result Code: %s - Result Message: %s' % (
            str(self.data.get('res')), self.data.get('res_message')))
        if self.debug_info is not None:
            for k, v in self.data['debug_info'].items():
                logging.debug('%s - %s' % (str.upper(k), str.replace(v, '<br/>', '\n')))

    def get_res(self):
        return self.res

    def get_rule_id(self):
        return self.rule_id

    def get_res_message(self):
        return self.res_message

    def get_debug_info(self):
        return self.debug_info


class CertResponse:
    def __init__(self, data):
        self.data = data
        self.res = data.get('res')
        self.res_message = data.get('res_message')
        self.debug_info = data.get('debug_info')
        self.details = self.debug_info.get('details')

    def log(self):
        logging.debug('Result Code: %s - Result Message: %s' % (
            str(self.data.get('res')), self.data.get('res_message')))
        print('Certificate Deatils: \n  Active: {active}\n  Experation Date: {expirationDate}'
              '\n  Revocation Error: {revocationError}\n  Validity Error: {validityError}'
              '\n  Chain Error: {chainError}\n  Hostname Mismatch Error: {hostnameMismatchError}'. format(**self.details))
