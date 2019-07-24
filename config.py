class Configuration(object):
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQL_USER = 'db_username'
	SQL_PASSWORD = 'db_userpass'
	SQL_HOST = 'db_host'
	SQL_DBNAME = 'db_name'
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(SQL_USER,SQL_PASSWORD,SQL_HOST,SQL_DBNAME)

class Mail_config(object):
	EMAIL_USER = 'user@someserver.com'  
	EMAIL_PASSWORD = 'qwerty'

class Checker_config(object):
	CHECKER_KEY = ''
	CHECKER_PERIOD = 10  
	CHECKER_MAILSEND_PAUSE = 3
