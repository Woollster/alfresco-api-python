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

    def test_get_sites(self):
        sites = self.client.get_sites()
        self.assertIsInstance(sites, list)
        for site in sites:
            self.assertTrue('entry' in site)
            self.assertTrue('role' in site['entry'])
            self.assertTrue('visibility' in site['entry'])
            self.assertTrue('guid' in site['entry'])
            self.assertTrue('description' in site['entry'])
            self.assertTrue('id' in site['entry'])
            self.assertTrue('title' in site['entry'])

    def test_get_site(self):
        site = self.client.get_site('swsdp')
        self.assertIsInstance(site, dict)
        self.assertTrue('role' in site)
        self.assertTrue('visibility' in site)
        self.assertTrue('guid' in site)
        self.assertTrue('description' in site)
        self.assertTrue('id' in site)
        self.assertTrue('title' in site)

    def test_add_site(self):
        site_id = input('Enter a site_id: ')
        response = self.client.add_site(
            site_id=site_id,
            title='Test Site',
            description='This is a test site.',
            role='SiteManager'
        )
        print(response)
        self.assertTrue(response)
        response = self.client.delete_site(site_id)
        print(response)

    def test_update_site(self):
        site_id = input('Enter a site_id: ')
        response = self.client.add_site(
            site_id=site_id,
            title='Test Site',
            description='This is a test site.',
            role='SiteManager'
        )
        print(response)
        self.assertTrue(response)

        response = self.client.update_site(
            site_id=site_id,
            title='Updated Test Site',
            description='This is an updated test site',
            role='SiteConsumer',
            visibility='MODERATED',
        )
        print(response)
        response = self.client.delete_site(site_id)
        print(response)


class PeopleTestCase(unittest.TestCase):
    def setUp(self):
        self.client = AlfApiClient(HOSTNAME, USERNAME, PASSWORD)

    def test_add_person(self):
        response = self.client.add_person(
            user_id='testuser1',
            first_name='Test',
            last_name='User1',
            email='testuser1@localhost',
            password='admin',
        )
        self.assertTrue(
            response.status_code == 201 or
            response.status_code == 409
        )
        print(response.status_code)

        response = self.client.add_person(
            user_id='testuser2',
            first_name='Test',
            last_name='User2',
            email='testuser2@localhost',
            password='admin',
        )
        self.assertTrue(
            response.status_code == 201 or
            response.status_code == 409
        )
        print(response.status_code)


if __name__ == '__main__':
    # unittest.main()
    tts = TestSuite()

    # tts.addTests(TestLoader().loadTestsFromTestCase(AlfApiSiteTestCase))
    tts.addTests(TestLoader().loadTestsFromTestCase(PeopleTestCase))

    unittest.TextTestRunner(failfast=True).run(tts)
