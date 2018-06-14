class IncapRule:
    def __init__(self, data):
        self.id = 0
        self.name = ''
        self.action = ''
        self.filter = ''
        from Sites.cIncapRule import create
        for incapRule in data:
            print('--------------------------------------------------------------------------------------------')
            name = incapRule['name']
            logger.info("Add %s InacapRule." % name)
            del incapRule['creation_date']
            del incapRule['id']
            incapRule['filter'] = incapRule['rule']
            del incapRule['rule']
            incapRule['site_id'] = site_id
            incapRule['action'] = str.upper(incapRule.get('action').replace('api.rule_action_type.', ''))
            from pprint import pprint
            # pprint(incapRule)
            result = create(incapRule)
            # pprint(result)
            if result['res'] == '0':
                logger.info("Successfully added %s!" % name)
            else:
                logger.error('Failed to add %s - %s' % (name, incapRule))
                err = IncapError(result)
                err.log()