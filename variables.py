class VARIABLES:  
    notified = False
    stored_log_vars = []

    @classmethod
    def append_stored_log_vars(cls, log_var):
        cls.stored_log_vars.append(log_var)

    @classmethod
    def clear_stored_log_vars(cls):
        cls.stored_log_vars = []

    @classmethod
    def set_notified(cls):
        cls.notified = not cls.notified

    @classmethod
    def get_notified(cls):
        return cls.notified
