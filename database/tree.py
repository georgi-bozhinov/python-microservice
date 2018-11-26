""" Read address books tree """
import os
import requests

node_backend = os.getenv('NODE_BACKEND', 'localhost:3000')


def _format_address(address):
    first_name = address[1]
    last_name = address[2]
    name = '{} {}'.format(first_name, last_name)

    return {
        'id': address[0],
        'first_name': first_name,
        'last_name': last_name,
        'phone': address[3], 'city': address[4],
        'name': name
    }


def _fetch_addresses(conn, bookid):
    sql = 'select id, first_name, last_name, phone, city from addresses where book=$1'
    stmt = conn.prepare(sql)

    addresses = []
    res = stmt(bookid)
    if res:
        for address in res:
            addresses.append(_format_address(address))

    return addresses


def _read_books(conn):
    sql = 'select * from books;'
    stmt = conn.prepare(sql)
    books = stmt()

    return books


def read(conn):
    """ all address books from DB """

    books = _read_books(conn)

    root = {}
    for book in books:
        book_id = book['id']
        book_node = {'name': book['name']}

        for address in _fetch_addresses(conn, book_id):
            address_id = str(address['id'])
            book_node[address_id] = address

        root[book_id] = book_node

    return {'books': root}
