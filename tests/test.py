#!/usr/bin/env python

import sys
import unittest
from unittest import TestSuite, TestLoader


sys.path.append('.')
sys.path.append('../')

from alfapi.alfapi import AlfRepo


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'


class AlfApiSiteTestCase(unittest.TestCase):

    def setUp(self):
        self.repo = AlfRepo(HOSTNAME, USERNAME, PASSWORD)


class PeopleTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = AlfRepo(HOSTNAME, USERNAME, PASSWORD)


if __name__ == '__main__':
    # unittest.main()
    tts = TestSuite()

    # tts.addTests(TestLoader().loadTestsFromTestCase(AlfApiSiteTestCase))
    # tts.addTests(TestLoader().loadTestsFromTestCase(PeopleTestCase))

    unittest.TextTestRunner(failfast=True).run(tts)
