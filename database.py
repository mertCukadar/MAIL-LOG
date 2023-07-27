from settings import DATABASE_CONF
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import sql

class QUERY:
    def __init__(self, query, schema, table):
        self.query = query
        self.schema = schema
        self.table = table

class DATABASE(QUERY):
    def connect_database(self):
        conn = psycopg2.connect(
            database=DATABASE_CONF.DATABASES['default']['NAME'],
            user=DATABASE_CONF.DATABASES['default']['USER'],
            password=DATABASE_CONF.DATABASES['default']['PASSWORD'],
            host=DATABASE_CONF.DATABASES['default']['HOST'],
            port=DATABASE_CONF.DATABASES['default']['PORT'],
        )

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        try:
            
            cursor.execute("SELECT 1")
            conn.commit()
        except (psycopg2.OperationalError, psycopg2.InterfaceError):
            print("CONNECTION FAILED")
           

        return conn

    def collect_data(self):
        conn = self.connect_database()
        cursor = conn.cursor()

        
        query = sql.SQL("SELECT * FROM {}.{};").format(
            sql.Identifier(self.schema),
            sql.Identifier(self.table)
        )

        cursor.execute(query)
        collected_log_vars = cursor.fetchall()

        
        conn.close()

        return collected_log_vars
