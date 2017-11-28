#!/usr/bin/env python

import json
import sys
import unittest

from requests.models import Response

sys.path.append('../')

from alfapi.alfapi import AlfApiClient


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'


class AlfApiTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_sites(self):
        client = AlfApiClient(HOSTNAME, USERNAME, PASSWORD)
        sites = client.get_sites()
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
        client = AlfApiClient(HOSTNAME, USERNAME, PASSWORD)
        site = client.get_site('swsdp')
        self.assertIsInstance(site, dict)
        self.assertTrue('role' in site)
        self.assertTrue('visibility' in site)
        self.assertTrue('guid' in site)
        self.assertTrue('description' in site)
        self.assertTrue('id' in site)
        self.assertTrue('title' in site)


if __name__ == '__main__':
    unittest.main()
