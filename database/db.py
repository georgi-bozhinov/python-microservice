import postgresql.driver as pg_driver

from .config import CREDENTIALS


class DatabaseManager:
    def __init__(self):
        self.conn = pg_driver.connect(**CREDENTIALS)

    def __enter__(self):
        return self

    def __exit__(self, _type, value, traceback):
        self.conn.close()