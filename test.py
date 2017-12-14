#!/usr/bin/env python

import json

from alfapi.alfapi import (
    AlfRepo, PersonRequest, SiteRequest, GroupRequest, ActivitiesRequest, TagRequest,
    NodeRequest
)


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'


if __name__ == '__main__':
    repo = AlfRepo(HOSTNAME, USERNAME, PASSWORD)

    """
    person_request = PersonRequest(repo)
    
    print(person_request.get('admin'))

    print(person_request.get_all())

    user_dict = {
        'id': 'hseritt2',
        'firstName': 'Harlin',
        'email': 'hseritt@formtek.com',
        'password': 'admin',
    }
    
    print(person_request.post(user_dict))

    user_dict = {
        'email': 'harlin.seritt@gmail.com',
    }

    print(person_request.put('hseritt2', user_dict))

    print(person_request.delete('hseritt2'))
    """

    """
    site_request = SiteRequest(repo)

    print(site_request.get_all())

    site_dict = {
        'title': 'testsite2',
        'visibility': 'PUBLIC',
    }
    print(site_request.post(site_dict).content)

    site_dict = {
        'title': 'testsite-extra',
        'visibility': 'PRIVATE'
    }
    print(site_request.put('testsite2', site_dict).content)

    print(site_request.delete('testsite1'))
    print(site_request.delete('testsite2'))
    """

    """
    group_request = GroupRequest(repo)

    print(group_request.get_all().content)
    print(group_request.get('GROUP_ALFRESCO_ADMINISTRATORS').content)

    group_dict = {
        'id': 'testgroup1'
    }

    print(group_request.post(data=group_dict).content)

    group_dict = {
        'displayName': 'Just another group',
    }

    print(group_request.put('GROUP_testgroup1', data=group_dict).content)

    print(group_request.delete('GROUP_testgroup1'))
    """

    """
    activities_request = ActivitiesRequest(repo)
    print(activities_request.get_all('admin').content)
    """

    """
    tags_request = TagRequest(repo)
    print(tags_request.get_all().content)
    print(tags_request.get('73530c67-613a-4b14-a788-839ad9ff9ed4').content)

    tag_data = {
        'tag': 'cert'
    }

    print(tags_request.put('73530c67-613a-4b14-a788-839ad9ff9ed4', data=tag_data).content)
    """

    node_request = NodeRequest(repo)

    children = json.loads(
        node_request.children('-root-').content
    )['list']['entries']
    
    for child in children:
        if child['entry']['name'] == 'TestFolder':
            test_folder_id = child['entry']['id']

    print(node_request.get(test_folder_id).content)

    node_dict = {
        'name': input('Enter a document name with extension: '),
        'nodeType': 'cm:content'
    }

    print(node_request.post(test_folder_id, node_dict).content)

    children = (json.loads(node_request.children(test_folder_id).content)['list']['entries'])

    node_dict = {
        'title': 'This is my test document!'
    }

    print(node_request.put(test_folder_id, node_dict).content)

    for child in children:
        print(node_request.delete(child['entry']['id']))
    