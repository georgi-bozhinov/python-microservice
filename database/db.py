import postgresql.driver as pg_driver

from .config import CREDENTIALS


class DatabaseManager:
    def __init__(self):
        self.conn = pg_driver.connect(**CREDENTIALS)
        init_tables(self.conn)

    def __enter__(self):
        return self

    def __exit__(self, _type, value, traceback):
        self.conn.close()


def init_tables(conn):
        conn.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );

        CREATE TABLE IF NOT EXISTS addresses (
            id SERIAL PRIMARY KEY,
            book INTEGER REFERENCES books(id),
            first_name VARCHAR(256),
            last_name VARCHAR(256),
            address VARCHAR(256),
            city VARCHAR(256),
            country VARCHAR(256),
            zip VARCHAR(10),
            phone VARCHAR(25),
            email VARCHAR(50),
            web VARCHAR(50)
        );
        """
        )
