from database import DATABASE , QUERY

if __name__ == '__main__':

    # Create an instance for the QUERY class
    query_vars = QUERY('public', 'alarms')
    
    # Create an instance for the DATABASE class
    conn = DATABASE.connect_database(self=query_vars)
    collected_log_vars = DATABASE.collect_data(self=query_vars , conn=conn)
    print(collected_log_vars)