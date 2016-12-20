import sys
import unittest

sys.path.insert(0, sys.path[0]+"/..")

import harvest


class TestHarvest(unittest.TestCase):
    def setUp(self):
        self.harvest = harvest.Harvest("https://goretoytest.harvestapp.com", "tester@goretoy.com", "tester account")

    def tearDown(self):
        pass

    def test_status_not_down(self):
        self.assertEqual("none", self.harvest.status['indicator'], "Harvest API is having problems")

if __name__ == '__main__':
    unittest.main()
