from settings import DATABASE_CONF
import psycopg2
from psycopg2.extras import RealDictCursor

class DATABASE:
    def connect_database():
        conn = psycopg2.connect(
        database = DATABASE_CONF.DATABASES['default']['NAME'],
        user = DATABASE_CONF.DATABASES['default']['USER'],
        password = DATABASE_CONF.DATABASES['default']['PASSWORD'],
        host = DATABASE_CONF.DATABASES['default']['HOST'],
        port = DATABASE_CONF.DATABASES['default']['PORT'],
    )

        cursor= conn.cursor(cursor_factory = RealDictCursor)

        try:
            cursor.execute("SELECT 1")
            conn.commit()
        except (psycopg2.OperationalError , psycopg2.InterfaceError):
            print("CONNECTION FAILED")
