import unittest
from Sites.site import Site
from Utils.incapResponse import IncapResponse
from Utils.clidriver import testing
import Utils.log
import logging


class TestIncapCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = None
        cls.incapresponse = IncapResponse(
            {
                "res": 0,
                "res_message": "OK",
                "debug_info": {
                    "id-info": "13007"
                }
            }

        )
        cls.site_id = None
        cls.site = Site(
            {
                "domain": "www.saic.com",
                "site_id": 0
            }
        )

    def test_site_add(self):
        logging.basicConfig(format='%(levelname)s - %(message)s')
        TestIncapCLI.site_id = testing(['site', 'add', TestIncapCLI.site.domain]).site_id
        self.assertNotEqual(TestIncapCLI.site_id, None, 'The site ID is not new.')
        logging.debug(str(TestIncapCLI.site_id))

    def test_site_b_status(self):
        logging.basicConfig(format='%(levelname)s - %(message)s')
        TestIncapCLI.site_id = testing(['site', 'status', str(TestIncapCLI.site_id)]).site_id
        self.assertNotEqual(TestIncapCLI.site_id, None, 'The site ID is None.')
        logging.debug(str(TestIncapCLI.site_id))

    def test_site_c_delete(self):
        logging.basicConfig(format='%(levelname)s - %(message)s')
        TestIncapCLI.res = testing(['site', 'delete', str(TestIncapCLI.site_id)]).res
        self.assertNotEqual(TestIncapCLI.incapresponse.res, None, 'The site ID is None.')
        logging.debug(str(TestIncapCLI.incapresponse.res_message))
    #
    # def test_site_c_list(self):
    #     res = testing(['site', 'list'])
    #     self.assertNotEqual(res, None, 'The site list is None.')
    #     logging.debug(str(res))
    #
    # def test_site_configure(self):
    #     res = testing(['site', 'configure', 'seal_location', 'api.seal_location.bottom_right', str(TestIncapCLI.site_id)])
    #     self.assertEqual(res, 0, 'The site configuration is None.')
    #     logging.debug(str(res))
    #
    # @classmethod
    # def tearDownClass(cls):
    #     TestIncapCLI.site_id = testing(['site', 'delete', str(TestIncapCLI.site_id)])
    #     logging.debug(str(TestIncapCLI.site_id))
    #     TestIncapCLI.assertNotEqual(TestIncapCLI.site_id, None, 'The site was not deleted.')


if __name__ == '__main__':
    unittest.main()


