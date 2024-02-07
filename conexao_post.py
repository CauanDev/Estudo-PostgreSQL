import psycopg2

conn = psycopg2.connect(
    database = 'fiperama',
    user = 'postgres',
    password = '1234',
    host = 'localhost',
    port = '5432'
)