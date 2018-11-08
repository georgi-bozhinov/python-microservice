import os


CREDENTIALS = {
    'database': os.getenv('POSTGRES_DB', 'test'),
    'user': os.getenv('POSTGRES_USER', 'testuser'),
    'password': os.getenv('POSTGRES_PASSWORD', 'testpassword'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': '5432'
}
