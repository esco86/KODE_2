import requests, time
from models import Tickers, db
from mail_send import send_mail
from config import Checker_config


def get_ticker_price(ticker_name: str) -> float:
	url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(ticker_name,Checker_config.CHECKER_KEY)
	r = requests.get(url)
	try:
		res = float(r.json()['Global Quote']['05. price'])
	except:
		res = None
 
	return res

def get_tickers():
	return Tickers.query.all()

def get_subcr(ticker):
	return ticker.subscribe

# def check_ticker(ticker: str):
# 	pass

def delete_subscr(s):
	db.session.delete(s)
	db.session.commit()	

def check_db_exist():
	try:
		Users.query.first()
	except:
		db.create_all()

def run_check():
	check_db_exist()
	while True:
		db.session.commit()
		all_tick = get_tickers()
		notifs = []
		for x in all_tick:
			subs = get_subcr(x)
			price = get_ticker_price(x.name)
			if price:
				for s in subs:
					if s.max_price:
						if price>s.max_price:
							notifs.append(dict(user = s.user.email, message = 'The price of {} risen higher  {}.\nPrice is - {}'.format(x.name,s.max_price, price)))
							delete_subscr(s)
					if s.min_price:
						if price<s.min_price:
							notifs.append(dict(user = s.user.email, message = 'The price of {} dropped bellow {}.\nPrice is - {}'.format(x.name,s.min_price, price)))
							delete_subscr(s)
		for n in notifs:
			send_mail(n)
			time.sleep(Checker_config.CHECKER_MAILSEND_PAUSE)
		time.sleep(Checker_config.CHECKER_PERIOD)



if __name__ == '__main__':
	run_check()
	# print(get_ticker_info('ACB'))