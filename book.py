import os
from random import randint

import requests

# def _insert_book(conn):
#     book_id = randint(1, 100000)
#     book_name = 'My Book #{}'.format(str(book_id))

#     sql = 'insert into books values ($1, $2);'
#     stmt = conn.prepare(sql)
#     stmt(book_id, book_name)

#     return book_id


node_backend = os.getenv('NODE_BACKEND', 'localhost:3000')


def _insert_addresses(conn, bookid):
    sql = 'insert into addresses \
        values ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);'

    addressid = randint(1, 100000)
    stmt = conn.prepare(sql)
    stmt(
        addressid,
        bookid,
        'John',
        'Doe',
        'Dietmar-Hopp-Allee 16',
        'Walldorf',
        'Germany',
        '69169',
        '+49 6227 7 12345',
        'john.doe@sap.com',
        'https://sap.de'
    )

    addressid = randint(1, 100000)
    stmt = conn.prepare(sql)
    stmt(
        addressid,
        bookid,
        'Max',
        'Mustermann',
        'Dietmar-Hopp-Allee 16',
        'Walldorf',
        'Germany',
        '69169',
        '+49 6227 7 54321',
        'john.doe@sap.com',
        'https://sap.de'
    )


def insert_sample_data(conn):
    """ inserts two address books in DB """

    bookid = requests.get(f'http://{node_backend}/api/addressbook/books/insert').json()['book_id'][0]
    _insert_addresses(conn, bookid)


def delete_sample_data(conn):
    """ deletes database content """

    conn.execute('delete from addresses;')
    requests.get(f'http://{node_backend}/api/addressbook/books/delete')
