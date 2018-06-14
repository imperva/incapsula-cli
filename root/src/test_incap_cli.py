import unittest
from Sites.site import Site
from Utils.clidriver import testing
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


class TestIncapCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site_id = None
        cls.site = Site(
            {
                "domain": "www.saic.com",
                "site_id": 0
            }
        )

    def test_site_add(self):
        TestIncapCLI.site_id = testing(['site', 'add', TestIncapCLI.site.domain]).site_id
        self.assertNotEqual(TestIncapCLI.site_id, None, 'The site ID is not new.')
        logger.debug(str(TestIncapCLI.site_id))
    #
    # def test_site_b_status(self):
    #     TestIncapCLI.site_id = testing(['site', 'status', str(TestIncapCLI.site_id)]).site_id
    #     self.assertNotEqual(TestIncapCLI.site_id, None, 'The site ID is None.')
    #     logger.debug(str(TestIncapCLI.site_id))
    #
    # def test_site_c_list(self):
    #     res = testing(['site', 'list'])
    #     self.assertNotEqual(res, None, 'The site list is None.')
    #     logger.debug(str(res))
    #
    # def test_site_configure(self):
    #     res = testing(['site', 'configure', 'seal_location', 'api.seal_location.bottom_right', str(TestIncapCLI.site_id)])
    #     self.assertEqual(res, 0, 'The site configuration is None.')
    #     logger.debug(str(res))

    # @classmethod
    # def tearDownClass(cls):
    #     TestIncapCLI.site_id = testing(['site', 'delete', str(TestIncapCLI.site_id)])
    #     logger.debug(str(TestIncapCLI.site_id))
    #     TestIncapCLI.assertNotEqual(TestIncapCLI.site_id, None, 'The site was not deleted.')


if __name__ == '__main__':
    unittest.main()


