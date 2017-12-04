#!/usr/bin/env python

from alfapi.alfapi import AlfRepo


HOSTNAME = 'http://localhost:8080'
USERNAME = 'admin'
PASSWORD = 'admin'


if __name__ == '__main__':
    repo = AlfRepo(HOSTNAME, USERNAME, PASSWORD)

    username = 'hseritt'

    """
    person = repo.people.add(
        id=username,
        email='hseritt@formtek.com',
        password='admin',
        firstName='Harlin',
        lastName='Seritt',
    )
    """

    #"""
    people_list = repo.people.all()
    for person in people_list:
        for attr in dir(person):
            if not attr.startswith('__'):
                print(
                    '{}: {}'.format(
                        attr,
                        getattr(person, attr)
                    )
                )
        print('\n')
    #"""

    #"""
    person = repo.people.get(username)
    for attr in dir(person):
        if not attr.startswith('__'):
            print(
                '{}: {}'.format(
                    attr,
                    getattr(person, attr)
                )
            )
    print('\n')
    #"""

    #"""
    person = repo.people.update(username, {'firstName': 'Philip'})
    for attr in dir(person):
        if not attr.startswith('__'):
            print(
                '{}: {}'.format(
                    attr,
                    getattr(person, attr)
                )
            )
    print('\n')
    #"""
