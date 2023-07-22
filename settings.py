#EMAIL_HOST CLASS  

class EMAIL_HOST:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '<host user>'
    EMAIL_HOST_PASSWORD = '<host password>'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

#DATABASE CLASS

class DATABASE_CONF:
    DATABASES = {"default": {"NAME": "db_name",
                            "USER": "db_user",
                            "PASSWORD": "db_password",
                            "HOST": "db_host",
                            "PORT": "db_port"}} 

#LOG CLASS


