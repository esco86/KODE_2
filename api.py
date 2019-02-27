
from app import app
from models import *
from flask import request, jsonify


def add_user(email:str):
	user = Users(email = email)
	db.session.add(user)
	db.session.commit()

def check_user(email:str):
	return bool(Users.query.filter(Users.email.contains(email)).first())

def del_user(email:str):
	user = Users.query.filter(Users.email.contains(email)).first()
	db.session.delete(user)
	db.session.commit()


def add_ticker(ticker:str):
	tick = Tickers(name = ticker)
	db.session.add(tick)
	db.session.commit()

def check_ticker(ticker:str):
	return bool(Tickers.query.filter_by(name = ticker).first())



def add_subscr(r):
	try:
		n_max = r['max_price']
	except:
		n_max = None
	try:
		n_min = r['min_price']
	except:
		n_min = None
	user = Users.query.filter_by(email = r['email']).first()
	ticker = Tickers.query.filter_by(name = r['ticker']).first()
	subscr = Subscribes(ticker = ticker.id, max_price = n_max, min_price = n_min, owner = user.id)
	db.session.add(subscr)
	db.session.commit()

def del_subscr(email, ticker):
	user = Users.query.filter_by(email = email).first()
	ticker = Tickers.query.filter_by(name = ticker).first()
	subscr = Subscribes.query.filter_by(owner = user.id, ticker = ticker.id).first()
	db.session.delete(subscr)
	db.session.commit()	



@app.route('/subscription', methods=['POST'])
def subscribe():
	r = request.get_json()

	if not check_user(r['email']):
		add_user(r['email'])
	if not check_ticker(r['ticker']):
		add_ticker(r['ticker'])
	usr = Users.query.filter_by(email = r['email']).first()
	
	if len(usr.subscribes)<5:
		add_subscr(r)

	return jsonify(r)
	
@app.route('/subscription', methods=['DELETE'])
def delete_subscr():
	email = request.args.get('email')
	ticker = request.args.get('ticker')

	if ticker:
		del_subscr(email, ticker)
	else:
		del_user(email)

	return 'HTTP/1.1 200 OK\n\n email - {} \n\n ticker - {}'.format(email, ticker).encode()



def run_api():
		app.run()

if __name__ == '__main__':
	app.run()
	# print('Hello')