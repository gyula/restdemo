import unittest
from client import Repoclient
from dotenv import Dotenv

class ClientTestcase(unittest.TestCase):
    def setUp(self):
        try:
            cmd_conf = Dotenv('./cmd-conf')
            self.APIaddress = cmd_conf['APIaddress']
            self.client = Repoclient(self.APIaddress)
        except IOError:
            env = os.environ

    def tearDown(self):
        pass

    def __createdummy(self):
        for i in range(5):
            res = self.client.createRepo("Test Repo", "Test User")
            if i % 2 == 0:
                res_id = res['id']
                for i in range(5):
                    self.client.getRepoDetails(res_id)

    def test_01_create(self):
        """Test: create repository """
        res = self.client.createRepo("Test Repo", "Test User")
        id = res['id']
        rname = "Test Repo"
        response = self.client.getRepoDetails(id)
        self.assertEqual(response['name'], rname)

    def test_02_request(self):
        """Test: Get the first repository detail."""
        response = self.client.getRepoDetails(1)
        self.assertEqual(response['name'], 'Test Repo')

    def test_03_delete(self):
        """Test: Delete the first repository """
        self.client.deleteRepo(1)
        response = self.client.getRepoDetails(1)
        self.assertEqual(response, None)

    def test_04_check_counter(self):
        """Test: check if counter incremented by one after access """
        res = self.client.createRepo("Test Repo", "Test User")
        id = res['id']
        response_first = self.client.getRepoDetails(id)
        response_second = self.client.getRepoDetails(id)
        self.assertTrue(response_second['access_cnt'] > response_first['access_cnt'], msg=None)

    def test_05_list_by_access_cnt(self):
        """ Test: Check that if only those repos listed which were accessed at least N times  """
        cnt = 3
        self.__createdummy()
        res = self.client.getRepolist(cnt)
        isBigger = True
        for item in res:
            if item['access_cnt'] < cnt:
               isBigger = False
        self.assertTrue(isBigger, msg=None)

