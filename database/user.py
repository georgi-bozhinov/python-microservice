import os

import requests

node_backend = os.getenv('NODE_BACKEND', 'localhost:3000')


def get_users(conn):
   return requests.get(f'http://{node_backend}/userinfo').json()