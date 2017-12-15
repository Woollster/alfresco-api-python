#!/usr/bin/env python
""" Test module for alfapi."""

import base64
import json
import requests

from alfapi.alfapi import (
    AlfRepo, PeopleActivities, AuditApplications, AuditEntries, NodeChildren,
    NodeContent, Nodes, NodeCopy, NodeMove, NodeLock, NodeParents, NodeSources,
    NodeUnlock, NodeTargets, People, PeopleAvatar, PeoplePreferences, NodeQueries,
    PeopleQueries, SiteQueries
)


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'

if __name__ == '__main__':
    repo = AlfRepo(HOSTNAME, USERNAME, PASSWORD)

    # PeopleActivities tests based on Activities
    """
    people_activities = PeopleActivities(repo)
    print(people_activities.get('admin').content)
    """

    # AuditApplications
    """
    audit_apps = AuditApplications(repo)

    # testing get_all()
    apps = json.loads(audit_apps.get_all().content)['list']['entries']

    # testing get()
    for app in apps:
        app_id = app['entry']['id']
        print(app_id)
        print(audit_apps.get(app_id).content)
        
        # testing put()
        audit_app_dict = {'isEnabled': 'false'}
        print(audit_apps.put(app_id, audit_app_dict).content)

        audit_app_dict = {'isEnabled': 'true'}
        print(audit_apps.put(app_id, audit_app_dict).content)

        # AuditEntries
        # out of the box, there are none
        audit_entries = AuditEntries(repo)
        print(audit_entries.get_all(app_id).content)
    """

    # NodeChildren
    """
    node_children = NodeChildren(repo)
    test_folder_dict = {
        'name': 'TestFolder',
        'nodeType': 'cm:folder',
        'description': 'My test folder'
    }
    print(node_children.post('-root-', test_folder_dict).content)

    children = json.loads(node_children.get_all('-root-').content)['list']['entries']

    for child in children:
        node = child['entry']
        # print(node['name'], node['id'])
        if node['name'] == 'TestFolder':
            test_folder_id = node['id']

    print(test_folder_id)

    test_document_dict = {
        'name': 'TestDocument.txt',
        'description': 'A test document with text.',
        'nodeType': 'cm:content'
    }

    print(
        json.loads(
            node_children.post(test_folder_id, test_document_dict).content
        )
    )

    children = json.loads(node_children.get_all(test_folder_id).content)['list']['entries']

    for child in children:
        node = child['entry']
        # print(node['name'], node['id'])
        if node['name'] == 'TestDocument.txt':
            test_document_id = node['id']

    with open('test_document.txt', 'r') as fh:
        content = fh.read()

    # print(content)
    content_dict = {
        'body': content,
    }
    node_content = NodeContent(repo)
    print(node_content.put(test_document_id, data=content).content)

    print(node_content.get(test_document_id).content)

    nodes = Nodes(repo)
    print(nodes.get(test_document_id).content)

    updated_test_doc_dict = {
        'name': 'UpdatedTestDocument.txt',
        'title': 'Updated Test Document',
        'description': 'This is an updated test document'
    }

    print(nodes.put(test_document_id, updated_test_doc_dict).content)

    new_folder_dict = {
        'name': 'NewFolder',
        'description': 'For testing copies and moves.',
        'nodeType': 'cm:folder'
    }

    print(node_children.post(test_folder_id, new_folder_dict).content)

    children = json.loads(node_children.get_all(test_folder_id).content)['list']['entries']

    for child in children:
        node = child['entry']
        # print(node['name'], node['id'])
        if node['name'] == 'NewFolder':
            new_folder_id = node['id']

    # print(new_folder_id)

    node_copy = NodeCopy(repo)
    target_dict = {
        'targetParentId': new_folder_id,
    }
    print(node_copy.post(test_document_id, target_dict).content)
    
    moved_folder_dict = {
        'name': 'MovesFolder',
        'nodeType': 'cm:folder',
        'description': 'My folder for testing moves'
    }
    print(node_children.post(test_folder_id, moved_folder_dict).content)

    children = json.loads(node_children.get_all(test_folder_id).content)['list']['entries']

    for child in children:
        node = child['entry']
        print(node['name'], node['id'])
        if node['name'] == 'MovesFolder':
            moved_folder_id = node['id']

    # print(moved_folder_id)
    node_move = NodeMove(repo)
    target_dict = {
        'targetParentId': moved_folder_id
    }
    print(node_move.post(test_document_id, target_dict).content)

    children = json.loads(node_children.get_all(moved_folder_id).content)['list']['entries']

    print("THESE...")
    for child in children:
        node = child['entry']
        print(node['name'], node['id'])
        if node['name'] == 'TestDocument.txt':
            moved_test_doc_id = node['id']

    # print(moved_test_doc_id)
    
    test_document_dict = {
        'name': 'NewTestDocument.txt',
        'description': 'A test document with text.',
        'nodeType': 'cm:content'
    }

    print(
        json.loads(
            node_children.post(test_folder_id, test_document_dict).content
        )
    )

    children = json.loads(node_children.get_all(test_folder_id).content)['list']['entries']

    for child in children:
        node = child['entry']
        # print(node['name'], node['id'])
        if node['name'] == 'NewTestDocument.txt':
            test_document_id = node['id']

    node_lock = NodeLock(repo)
    node_lock_dict = {
        'timeToExpire': 30,
        'type': 'ALLOW_OWNER_CHANGES',
        'lifetime': 'PERSISTENT'
    }
    print(node_lock.post(test_document_id, data=node_lock_dict).content)

    node_unlock = NodeUnlock(repo)
    print(node_unlock.post(test_document_id).content)

    node_parents = NodeParents(repo)
    print(node_parents.get_all(test_document_id).content)

    node_sources = NodeSources(repo)
    print(node_sources.get_all(test_document_id).content)

    node_targets = NodeTargets(repo)
    print(node_targets.get_all(test_document_id).content)

    targeted_dict = {
        'targetId': moved_test_doc_id,
        'assocType': 'MyAssociationType'
    }

    print(node_targets.post(test_document_id, data=targeted_dict).content)

    print(nodes.delete(test_document_id).content)
    print(nodes.delete(moved_test_doc_id).content)
    print(nodes.delete(test_folder_id).content)
    """


    # People requests
    """
    people = People(repo)
    print(people.get_all().content)

    people_dict = {
        'id': 'testuser1',
        'firstName': 'Test',
        'lastName': 'User1',
        'email': 'testuser1@localhost',
        'password': 'admin',
    }
    print(people.post(data=people_dict).content)

    people_dict = {
        'firstName': 'Bilbo',
        'lastName': 'Baggins',
    }

    print(people.put('testuser1', data=people_dict).content)

    print(people.get('testuser1').content)
    """

    # PeopleAvatar
    """
    people_avatar = PeopleAvatar(repo)

    image_file = open('avatar.png', 'rb')

    print(people_avatar.put('testuser1', data=image_file).content)

    image_file.close()

    print(people_avatar.get('testuser1').content)

    print(people_avatar.delete('testuser1').content)
    """

    # Password resets - probably won't use
    """
    password_reset_request = PeopleRequestResetPassword(repo)
    print(password_reset_request.post('testuser1', data={'client': 'share'}).content)
    """   

    # People preferences
    """
    people_preferences = PeoplePreferences(repo)
    print(people_preferences.get_all('testuser1').content)
    """

    # Queries
    """
    people_query = PeopleQueries(repo)
    print(people_query.get(params={'term': 'test'}).content)

    site_queries = SiteQueries(repo)
    print(site_queries.get(params={'term': 'test'}).content)

    node_queries = NodeQueries(repo)
    print(node_queries.get(params={'term': 'test'}).content)
    """

    
