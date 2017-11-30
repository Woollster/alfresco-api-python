""" Alfresco API module for Python.
"""

import json
import logging
import sys

import requests

logger = logging.getLogger('tests.alfapi')
logger.setLevel(logging.INFO)
log_format = logging.Formatter(
    '%(asctime)s  [%(levelname)s]  '
    '[%(module)s.%(name)s.%(funcName)s]:%(lineno)s'
    '  %(message)s'
)

console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)


URI = 'alfresco/api/-default-/public/alfresco/versions/1'


class Person(object):
    pass


class AlfApiClient(object):
    """ API Client """

    def _get_url(self, uri):
        return '{url}/{uri}'.format(
            url=self.url,
            uri=uri,
        )

    def __init__(self, host_url, username, password):
        self.url = '{host_url}/{uri}'.format(
            host_url=host_url,
            uri=URI
        )
        self.username = username
        self.password = password

    def people(self, method='GET', instance=None):
        """ People are users in an Alfresco system.
        Options for modes are:
        POST, GET, PUT, DELETE
        """
        if method == 'GET':
            if not instance:
                base_uri = 'people'
                response = requests.get(
                    self._get_url(base_uri),
                    auth=(
                        self.username, self.password
                    )
                )
                logger.debug(response)
                raw_data = [
                    entry['entry'] for entry in json.loads(
                        response.content
                    )['list']['entries']
                ]
                people = []
                person = Person()
                for person_dict in raw_data:
                    for k, v in person_dict.items():
                        setattr(person, k, v)
                    people.append(person)
                return people
            else:
                base_uri = '/'.join(['people', instance])
                response = requests.get(
                    self._get_url(base_uri),
                    auth=(
                        self.username, self.password
                    )
                )
                logger.debug(response)
                raw_data = json.loads(response.content)['entry']
                person = Person()
                for k, v in raw_data.items():
                    setattr(person, k, v)
                return person
