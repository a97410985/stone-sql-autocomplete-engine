import unittest


class TestFetchingCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls._connection = createExpensiveConnectionObject()
        print("setup")

    @classmethod
    def tearDownClass(cls):
        # cls._connection.destroy()
        print("teardown")

    def test_fetch_databases(self):
        self.assertTrue(True)
