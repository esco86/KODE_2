
import threading
from api import run_api
from checker import run_check




if __name__ == '__main__':
	t_app = threading.Thread(target = run_check, name='Thread_CHECKER')
	t_app.start()
	run_api()