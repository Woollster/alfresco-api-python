""" Alfresco API module for Python.
"""

import json
import logging
import sys

import requests

logger = logging.getLogger('alfapi')
logger.setLevel(logging.INFO)
log_format = logging.Formatter(
    '%(asctime)s  [%(levelname)s]  '
    '[%(module)s.%(name)s.%(funcName)s]:%(lineno)s'
    '  %(message)s'
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)


URI = 'alfresco/api/-default-/public/alfresco/versions/1'


def _get_url(url, base_path):
        return '{url}/{base_path}'.format(
            url=url,
            base_path=base_path,
        )


people_attributes = (
    'lastName', 'userStatus', 'jobTitle', 'statusUpdatedAt',
    'mobile', 'emailNotificationEnabled', 'description',
    'telephone', 'enabled', 'firstName', 'skypeId',
    'avatarId', 'location', 'company', 'id', 'email',
)


class Model(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value


class People(Model):
    base_path = 'people'

    def __init__(self, repo):
        self.repo = repo

    def add(self, **kwargs):
        url = _get_url(self.repo.url, self.base_path)
        response = requests.post(
            url,
            auth=(
                self.repo.username,
                self.repo.password
            ),
            data=json.dumps(
                kwargs
            )
        )

        if response.status_code == 200:
            entry = json.loads(response.content)['entry']
            p = Model()

            for k, v in entry.items():
                setattr(p, k, v)
            for attr in people_attributes:
                if not hasattr(p, attr):
                    if k is not 'company':
                        setattr(p, attr, None)
                    else:
                        setattr(p, attr, {})
            return p
        else:
            logger.warn(response.status_code)
            logger.warn(response.content)

    def all(self):
        url = _get_url(self.repo.url, self.base_path)
        response = requests.get(
            url,
            auth=(
                self.repo.username,
                self.repo.password
            )
        )
        entry_list = [
            entry['entry'] for entry in json.loads(
                response.content
            )
            ['list']
            ['entries']
        ]

        p_list = []
        for entry in entry_list:
            p = Model()
            for k, v in entry.items():
                setattr(p, k, v)
            for attr in people_attributes:
                if not hasattr(p, attr):
                    if k is not 'company':
                        setattr(p, attr, None)
                    else:
                        setattr(p, attr, {})
            p_list.append(p)
        return p_list

    def get(self, user_id):
        url = '{}/{}'.format(
            _get_url(self.repo.url, self.base_path),
            user_id
        )
        response = requests.get(
            url,
            auth=(
                self.repo.username,
                self.repo.password
            )
        )
        entry = json.loads(response.content)['entry']
        p = Model()
        for k, v in entry.items():
            setattr(p, k, v)
        for attr in people_attributes:
            if not hasattr(p, attr):
                if k is not 'company':
                    setattr(p, attr, None)
                else:
                    setattr(p, attr, {})
        return p

    def update(self, user_id, user_dict):
        url = '{}/{}'.format(
            _get_url(self.repo.url, self.base_path),
            user_id
        )
        response = requests.put(
            url,
            auth=(
                self.repo.username,
                self.repo.password
            ),
            data=json.dumps(
                user_dict
            )
        )
        entry = json.loads(response.content)['entry']
        p = Model()
        for k, v in entry.items():
            setattr(p, k, v)
        for attr in people_attributes:
            if not hasattr(p, attr):
                if k is not 'company':
                    setattr(p, attr, None)
                else:
                    setattr(p, attr, {})
        return p


class AlfRepo(object):
    """ API Client """

    def __init__(self, host_url, username, password):
        self.url = '{host_url}/{uri}'.format(
            host_url=host_url,
            uri=URI
        )
        self.username = username
        self.password = password
        self.people = People(self)
