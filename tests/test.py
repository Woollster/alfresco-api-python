#!/usr/bin/env python

import sys
import unittest
from unittest import TestSuite, TestLoader


sys.path.append('.')
sys.path.append('../')

from alfapi.alfapi import AlfApiClient


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'


class AlfApiSiteTestCase(unittest.TestCase):

    def setUp(self):
        self.client = AlfApiClient(HOSTNAME, USERNAME, PASSWORD)


class PeopleTestCase(unittest.TestCase):
    def setUp(self):
        self.client = AlfApiClient(HOSTNAME, USERNAME, PASSWORD)

    def test_people_get(self):
        entries = self.client.people('GET')
        for person in entries:
            self.assertTrue(hasattr(person, 'avatarId'))
            self.assertTrue(hasattr(person, 'company'))
            self.assertTrue(hasattr(person, 'description'))
            self.assertTrue(hasattr(person, 'email'))
            self.assertTrue(hasattr(person, 'emailNotificationsEnabled'))
            self.assertTrue(hasattr(person, 'enabled'))
            self.assertTrue(hasattr(person, 'firstName'))
            self.assertTrue(hasattr(person, 'id'))
            self.assertTrue(hasattr(person, 'jobTitle'))
            self.assertTrue(hasattr(person, 'lastName'))
            self.assertTrue(hasattr(person, 'location'))
            self.assertTrue(hasattr(person, 'mobile'))
            self.assertTrue(hasattr(person, 'skypeId'))
            self.assertTrue(hasattr(person, 'statusUpdatedAt'))
            self.assertTrue(hasattr(person, 'telephone'))
            self.assertTrue(hasattr(person, 'userStatus'))

    def test_person_get(self):
        person = self.client.people('GET', 'admin')
        # self.assertTrue(hasattr(person, 'avatarId'))
        # self.assertTrue(hasattr(person, 'company'))
        # self.assertTrue(hasattr(person, 'description'))
        self.assertTrue(hasattr(person, 'email'))
        self.assertTrue(hasattr(person, 'emailNotificationsEnabled'))
        self.assertTrue(hasattr(person, 'enabled'))
        # self.assertTrue(hasattr(person, 'firstName'))
        self.assertTrue(hasattr(person, 'id'))
        # self.assertTrue(hasattr(person, 'jobTitle'))
        # self.assertTrue(hasattr(person, 'lastName'))
        # self.assertTrue(hasattr(person, 'location'))
        # self.assertTrue(hasattr(person, 'mobile'))
        # self.assertTrue(hasattr(person, 'skypeId'))
        # self.assertTrue(hasattr(person, 'statusUpdatedAt'))
        # self.assertTrue(hasattr(person, 'telephone'))
        # self.assertTrue(hasattr(person, 'userStatus'))


if __name__ == '__main__':
    # unittest.main()
    tts = TestSuite()

    # tts.addTests(TestLoader().loadTestsFromTestCase(AlfApiSiteTestCase))
    tts.addTests(TestLoader().loadTestsFromTestCase(PeopleTestCase))

    unittest.TextTestRunner(failfast=True).run(tts)
