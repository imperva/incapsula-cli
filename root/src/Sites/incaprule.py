from Sites.cIncapRule import create
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class IncapRule:
    def __init__(self, data):
        self.id = 0
        self.name = ''
        self.action = ''
        self.filter = ''
        
        for incapRule in data:
            print('--------------------------------------------------------------------------------------------')
            self.id = incapRule.get('id')
            self.name = incapRule['name']
            self.filter = incapRule['rule']
            self.action = str.upper(incapRule.get('action'))#.replace('api.rule_action_type.', ''))
            logger.info("Add %s InacapRule." % self.name)
            from pprint import pprint
            print(self.id)
            print(self.name)
            print(self.filter)
            print(self.action)
            #result = create(incapRule)
            # pprint(result)
            # if result['res'] == '0':
            #     logger.info("Successfully added %s!" % name)
            # else:
            #     logger.error('Failed to add %s - %s' % (name, incapRule))
            #     err = IncapError(result)
            #     err.log()