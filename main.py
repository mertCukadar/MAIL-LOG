from database import DATABASE , QUERY
from mail import MailSend 
import time
from variables import VARIABLES


    
if __name__ == '__main__':
    
    while True:
        # Create an instance for the QUERY class
        query = """SELECT a.alarm_id, a.alarm_name, a.alarm_class, l.mailsent, l.currentstate , l.logdate
        FROM public.alarms a
        INNER JOIN logs.aalm_table l ON a.alarm_id = l.aalm_id
        WHERE NOT l.mailsent AND l.currentstate = 1;
        """
        query_vars = QUERY(query=query)
        
        # Create an instance for the DATABASE class
        conn = DATABASE.connect_database()
        
        #wait for 5 seconds before checking the alarm state
        time.sleep(3)

        
        try:
            collected_log_vars = DATABASE.collect_data(query_vars , conn=conn)
            
            
            if len(collected_log_vars) > 0 :
                for row in collected_log_vars:
                    VARIABLES.append_stored_log_vars(row)  

                # Send mail
                mail_to = 'cukadar.mertkaan@gmail.com'
                mail_subject = 'Soğutma Grubu Alarm Durumu'
                mail_body = ''
                mail_message = ''
                        

                check_mail = MailSend.sendmail(mail_to, mail_subject, mail_body, mail_message, data_list=VARIABLES.stored_log_vars , html_file_path='alarm_page.html')
                
                
                if VARIABLES.get_notified() == True:
                    VARIABLES.set_notified()

                for row in collected_log_vars:
                        if check_mail:
                            # Update the logs table
                            query = f"""UPDATE logs.aalm_table SET mailsent = true WHERE aalm_id = {row['alarm_id']}"""
                            query_vars = QUERY(query=query)
                            DATABASE.update_logs(query_vars , conn=conn)
            

          


            query = """SELECT a.alarm_id, a.alarm_name, a.alarm_class, l.mailsent, l.currentstate , l.logdate
            FROM public.alarms a
            INNER JOIN logs.aalm_table l ON a.alarm_id = l.aalm_id
            WHERE l.mailsent AND l.currentstate = 1;
            """
            query_vars = QUERY(query=query)
            active_alarm_vars = DATABASE.collect_data(query_vars , conn=conn)

            if len(active_alarm_vars) == 0 and VARIABLES.notified == False:
                
                
                if VARIABLES.get_notified() == False:
                    VARIABLES.set_notified()
                    
                data_list = []
                check_mail = MailSend.sendmail(mail_to, mail_subject, mail_body, mail_message, data_list=collected_log_vars , html_file_path='alarm_notify.html')
                
                if len(collected_log_vars) == 0:
                    VARIABLES.clear_stored_log_vars()
                    query2 = """UPDATE logs.aalm_table
                    SET mailsent = false
                    WHERE mailsent = true;
                    """
                    query_vars2 = QUERY(query=query2)
                    DATABASE.update_logs(query_vars2 , conn=conn)
               

               
            conn.close()       
            
        except:
            pass