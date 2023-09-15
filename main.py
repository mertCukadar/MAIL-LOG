from database import DATABASE , QUERY
from mail import MailSend 
import time
from variables import VARIABLES


    
if __name__ == '__main__':
    
    
    while True:
        try:
            # Create an instance for the QUERY class
            query = """SELECT a.alarm_id, a.alarm_name, a.alarm_class, l.currentstate , l.logdate
            FROM public.alarms a
            INNER JOIN logs.aalm_table l ON a.alarm_id = l.aalm_id
            WHERE l.currentstate = 1;
            """
            query_vars = QUERY(query=query)
            
            # Create an instance for the DATABASE class
            conn = DATABASE.connect_database()
            
            #wait for 5 seconds before checking the alarm state
            time.sleep(3)
        except:
            pass
        
        try:
            
            
            collected_log_vars = DATABASE.collect_data(query_vars , conn=conn)
            
            
           
            if len(collected_log_vars) > VARIABLES.get_len_stored_log_vars():
                VARIABLES.clear_stored_log_vars()
                
                for row in collected_log_vars:
                    VARIABLES.append_stored_log_vars(row)

                
               
                VARIABLES.set_notified_false()
                VARIABLES.set_mailsent_false()

           
                
            
                if VARIABLES.get_mail_sent() == False:
                    
                    # Send mail
                    mail_to = 'cukadar.mertkaan@gmail.com'
                    mail_subject = 'Soğutma Grubu Alarm Durumu'
                    mail_body = ''
                    mail_message = ''
                            

                    check_mail = MailSend.sendmail(mail_to, mail_subject, mail_body, mail_message, data_list=VARIABLES.stored_log_vars , html_file_path='alarm_page.html')
                    VARIABLES.set_mail_sent()

            
            VARIABLES.set_len_stored_log_vars(len(collected_log_vars))

            if len(collected_log_vars) == 0 and VARIABLES.get_notified() == False:
                   
                    
                    data_list = []
                    check_mail = MailSend.sendmail(mail_to, mail_subject, mail_body, mail_message, data_list=collected_log_vars , html_file_path='alarm_notify.html')
                    
                    VARIABLES.clear_stored_log_vars()
                    VARIABLES.set_len_stored_log_vars(0)
                    VARIABLES.set_notified_true()
                    VARIABLES.set_mailsent_false()   
                    
        except:
            pass    

                   
        
          


