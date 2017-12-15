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

    url_path = None
    
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


class ModelRequestInGET(ModelRequest):
    def get(self, pk):
        url =  self.url.format(pk)
        response = requests.get(
            url,
            auth=self.auth
        )
        return response


class ModelRequestLIST(ModelRequest):

    def get_all(self):
        url = self.url
        print(url)
        response = requests.get(
            url,
            auth=self.auth
        )
        return response


class ModelRequestInLIST(ModelRequest):

    def get_all(self, pk):
        url = self.url.format(pk)
        print(url)
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


class ModelRequestInPOST(ModelRequest):
    
    def post(self, pk, data=None):
        url = self.url.format(pk)
        print(url)
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


class ModelRequestInPUT(ModelRequest):

    def put(self, pk, data):
        url = self.url.format(pk)
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
        print(url)
        response = requests.delete(
            url,
            auth=self.auth
        )
        return response


class ModelRequestInDELETE(ModelRequest):

    def delete(self, pk):
        url = self.url.format(pk)
        response = requests.delete(
            url,
            auth=self.auth
        )
        return response


class PeopleActivities(ModelRequestInGET):
    """ User activities
    """
    url_path = 'people/{}/activities'
    

class AuditApplications(ModelRequestLIST, ModelRequestGET, ModelRequestPUT):
    """ Audit applications 
    * Supported only for 5.2.2 +
    """
    url_path = 'audit-applications'


class AuditEntries(ModelRequestInLIST, ModelRequestInDELETE):
    """ Audit entries for audit applications.
        ModelRequestInDELETE/.delete() is not tested.
        
        The following are not covered:

        DELETE /audit-applications/{auditApplicationId}/audit-entries/{auditEntryId}
            Permanently delete an audit entry
        GET /audit-applications/{auditApplicationId}/audit-entries/{auditEntryId} 
            Get audit entry
        GET /nodes/{nodeId}/audit-entries List audit entries for a node
    """
    url_path = 'audit-applications/{}/audit-entries'


class NodeChildren(ModelRequestInPOST, ModelRequestInLIST):
    """ Nodes are most any object in Alfresco."""
    url_path = 'nodes/{}/children'


class NodeContent(ModelRequestInPUT, ModelRequestInGET):
    """ Document content."""
    url_path = 'nodes/{}/content'

class Nodes(ModelRequestGET, ModelRequestPUT, ModelRequestDELETE):
    """ Node object."""
    url_path = 'nodes'


class NodeCopy(ModelRequestInPOST):
    """ Node copy request."""
    url_path = 'nodes/{}/copy'


class NodeMove(ModelRequestInPOST):
    """ Node move request."""
    url_path = 'nodes/{}/move'


class NodeLock(ModelRequestInPOST):
    """ Node lock request."""
    url_path = 'nodes/{}/lock'


class NodeUnlock(ModelRequestInPOST):
    """ Node unlock request."""
    url_path = 'nodes/{}/unlock'


class NodeParents(ModelRequestInLIST):
    """ Top folder for node."""
    url_path = 'nodes/{}/parents'


class NodeSources(ModelRequestInLIST):
    """ Node sources.
        Note: out of the box, there will be none.
    """
    url_path = 'nodes/{}/sources'


class NodeTargets(ModelRequestInLIST, ModelRequestInPOST):
    """ Node target associations.
        Note: out of the box, there will be none.

        The following are not covered:

        DELETE /nodes/{nodeId}/targets/{targetId} Delete node association(s)

        Shaky: Creating a target association. Need to figure out this kind of error:

        b'{
            "error":
                {
                    "errorKey":"Unknown assocType: MyAssociationType",
                    "statusCode":400,
                    "briefSummary":"11150195 Unknown assocType: MyAssociationType",
                    "stackTrace":
                        "For security reasons the stack trace is no longer displayed, but the property is kept for previous versions",
                    "descriptionURL":"https://api-explorer.alfresco.com"
                }
            }'
                
    """
    url_path = 'nodes/{}/targets'
