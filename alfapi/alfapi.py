""" Alfresco API module for Python.
"""

import json
import logging
import sys

import requests

logger = logging.getLogger('tests.alfapi')
logger.setLevel(logging.WARN)
log_format = logging.Formatter(
    '%(asctime)s  [%(levelname)s]  '
    '[%(module)s.%(name)s.%(funcName)s]:%(lineno)s'
    '  %(message)s'
)

console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)


URI = 'alfresco/api/-default-/public/alfresco/versions/1'


class AlfApiClient(object):
    """ API Client """
    def __init__(self, host_url, username, password):
        self.url = '{host_url}/{uri}'.format(
            host_url=host_url,
            uri=URI
        )
        self.username = username
        self.password = password

    def get_sites(self):
        uri = 'sites'
        url = '{url}/{uri}'.format(
            url=self.url,
            uri=uri,
        )
        response = requests.get(
            url, auth=(
                self.username, self.password
            )
        )
        json_data = json.loads(response.content)
        return json_data['list']['entries']

    def add_site(
            self, site_id, title, visibility='PUBLIC',
            description=None, role='SiteConsumer'):
        """ Not supported for Alfresco 5.1.x and older. """

        uri = 'sites'
        url = '{url}/{uri}'.format(
            url=self.url,
            uri=uri,
        )

        payload = {}
        payload['id'] = site_id
        payload['title'] = title
        payload['visibility'] = visibility
        payload['description'] = description
        payload['role'] = role

        response = requests.post(
            url, auth=(
                self.username, self.password
            ),
            data=json.dumps(payload),
        )
        json_data = json.loads(response.content)
        return json_data

    def get_site(self, site_id):
        uri = 'sites/{site_id}'.format(site_id=site_id)
        url = '{url}/{uri}'.format(
            url=self.url,
            uri=uri,
        )
        response = requests.get(
            url, auth=(
                self.username, self.password
            )
        )
        json_data = json.loads(response.content)
        return json_data['entry']

    def delete_site(self, site_id):
        uri = 'sites/{site_id}'.format(site_id=site_id)
        url = '{url}/{uri}'.format(
            url=self.url,
            uri=uri,
        )
        print(url)
        response = requests.delete(
            url,
            auth=(
                self.username,
                self.password
            ),
        )
        return response
