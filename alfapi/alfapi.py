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

class AlfRepo(object):
    """ API Client """

    def __init__(self, host_url, username, password):
        self.url = '{host_url}/{uri}'.format(
            host_url=host_url,
            uri=URI
        )
        self.username = username
        self.password = password


class ModelRequest(object):
    
    def __init__(self, repo):
        self.repo = repo
        self.url = '{}/{}'.format(
            self.repo.url,
            self.url_path
        )
        self.auth = (self.repo.username, self.repo.password)


class ModelRequestGET(ModelRequest):

    def get(self, pk):
        url =  '{}/{}'.format(
            self.url,
            pk
        )
        print(url)
        response = requests.get(
            url,
            auth=self.auth
        )
        return response

class ModelRequestLIST(ModelRequest):

    def get_all(self):
        url = self.url
        response = requests.get(
            url,
            auth=self.auth
        )
        return response

    
class ModelRequestPOST(ModelRequest):
    
    def post(self, data):
        url = self.url
        response = requests.post(
            url,
            auth=self.auth,
            data=json.dumps(data)
        )
        return response


class ModelRequestPUT(ModelRequest):

    def put(self, pk, data):
        url = '{}/{}'.format(
            self.url,
            pk
        )
        response = requests.put(
            url,
            auth=self.auth,
            data=json.dumps(data)
        )
        return response


class ModelRequestDELETE(ModelRequest):

    def delete(self, pk):
        url = '{}/{}'.format(
            self.url,
            pk
        )
        response = requests.delete(
            url,
            auth=self.auth
        )
        return response


class PersonRequest(ModelRequestGET, ModelRequestLIST, ModelRequestPOST, ModelRequestPUT):
    
    url_path = 'people'


class SiteRequest(ModelRequestGET, ModelRequestLIST, ModelRequestPOST, ModelRequestPUT, ModelRequestDELETE):

    url_path = 'sites'


class GroupRequest(ModelRequestGET, ModelRequestLIST, ModelRequestPOST, ModelRequestPUT, ModelRequestDELETE):

    url_path = 'groups'


class TagRequest(ModelRequestLIST, ModelRequestGET, ModelRequestPUT):

    url_path = 'tags'


class NodeRequest(ModelRequestGET, ModelRequestDELETE, ModelRequestPUT):

    url_path = 'nodes'

    def children(self, node_id):
        url_path = '{}/children'.format(node_id)
        url = '{}/{}'.format(self.url, url_path)
        print(url)
        response = requests.get(
            url,
            auth=self.auth
        )
        return response

    def post(self, node_id, data):
        url_path = '{}/children'.format(node_id)
        url = '{}/{}'.format(self.url, url_path)
        response = requests.post(
            url,
            auth=self.auth,
            data=json.dumps(data)
        )
        return response


class ActivitiesRequest(ModelRequestLIST):

    url_path = 'people/{}/activities'

    def __init__(self, repo):
        self.repo = repo
        self.url = '{}/{}'.format(
            self.repo.url,
            self.url_path
        )
        self.auth = (self.repo.username, self.repo.password)

    def get_all(self, user_id):
        url = self.url.format(user_id)
        print(url)
        response = requests.get(
            url,
            auth=self.auth
        )
        return response
