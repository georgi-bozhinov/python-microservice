""" Flask based web app exposing addressbook REST API's """
import os
import traceback
from flask import Flask
from flask import request
from flask import jsonify
from flask import g

from flask_cors import CORS

from database.db import DatabaseManager
import database.tree as tree
import database.book as book
import database.user as user

# pylint: disable=missing-docstring,protected-access

app = Flask(__name__) # pylint: disable=invalid-name
CORS(app)


@app.errorhandler(500)
def handle_error(err):
    traceback.print_exc()

    return jsonify({'error': str(err)}), 500


@app.route('/api/addressbook/tree')
def fetch_books_tree():
    with DatabaseManager() as db:
        books_tree = tree.read(db.conn)

    return jsonify(books_tree)


@app.route('/api/addressbook/insert')
def create_sample_data():
    with DatabaseManager() as db:
        book.insert_sample_data(db.conn)

    return jsonify({'status': 'success'})


@app.route('/api/addressbook/delete')
def delete_table_data():
    with DatabaseManager() as db:
        book.delete_sample_data(db.conn)

    return jsonify({'status': 'success'})


@app.route('/api/addressbook/userinfo')
def user_info():
    with DatabaseManager() as db:
        users = user.get_users(db.conn)

    return jsonify(users)


PORT = int(os.getenv("PORT", 9099))


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=PORT)
