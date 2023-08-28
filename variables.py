class VARIABLES:  
    notified = True
    mail_sent = False
    stored_log_vars = []
    len_stored_log_vars = 0

    @classmethod
    def append_stored_log_vars(cls, log_var):
        cls.stored_log_vars.append(log_var)

    @classmethod
    def clear_stored_log_vars(cls):
        cls.stored_log_vars.clear()

    @classmethod
    def set_notified_true(cls):
        cls.notified = True

    @classmethod
    def set_notified_false(cls):
        cls.notified = False


    @classmethod
    def get_notified(cls):
        return cls.notified
    
    @classmethod
    def set_mail_sent(cls):
        cls.mail_sent = not cls.mail_sent

    @classmethod
    def get_mail_sent(cls):
        return cls.mail_sent
    
    @classmethod
    def get_stored_log_vars(cls):
        return cls.stored_log_vars
    
    @classmethod
    def get_len_stored_log_vars(cls):
        return cls.len_stored_log_vars


    @classmethod
    def set_len_stored_log_vars(cls , len_stored_log_vars):
        cls.len_stored_log_vars = len_stored_log_vars
        return cls.len_stored_log_vars

    @classmethod

    def set_mailsent_false(cls):
        cls.mail_sent = False
        return cls.mail_sent
    
   
        