from settings import DATABASE_CONF
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import sql

class QUERY:
    def __init__(self, query=None):
        self.query = query
        

class DATABASE(QUERY):
    @staticmethod
    def connect_database():
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
            print("CONNECTION SUCCESSFUL")
        except (psycopg2.OperationalError, psycopg2.InterfaceError , psycopg2.DatabaseError , psycopg2.ProgrammingError ):
            print("CONNECTION FAILED")
           

        return conn
    
    @staticmethod
    def collect_data(query_vars , conn):
        try:
            cursor = conn.cursor(cursor_factory = RealDictCursor)

            
            query = sql.SQL(query_vars.query)


            cursor.execute(query)
            collected_log_vars = cursor.fetchall()


            return collected_log_vars
        except:
            print("Error from collect_data")

    @staticmethod
    def update_logs(query_vars, conn):
        try:
            cursor = conn.cursor()

            query = sql.SQL(query_vars.query)

            cursor.execute(query)

            conn.commit()  # Değişiklikleri veritabanına kaydedin
            
            return True

        except Exception as e:
            print("Error from update_logs: ", str(e))
            return False