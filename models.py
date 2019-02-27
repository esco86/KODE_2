
from app import db 


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True)
	subscribes = db.relationship('Subscribes', backref = 'user', lazy='select', passive_deletes=True)
	
	def __init__(self, *args, **kwargs):
	    super(Users, self).__init__(*args, **kwargs)

	def __repr__(self):
		return 'id: {}; email: {}; '.format(self.id, self.email)

class Subscribes(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	ticker = db.Column(db.Integer, db.ForeignKey('tickers.id', ondelete="CASCADE"))
	max_price = db.Column(db.Float)
	min_price = db.Column(db.Float)
	owner = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
	# tick = db.relationship('Tickers', backref = 'subscribe', passive_deletes=True)
	tick = db.relationship('Tickers', backref = 'subscribe')

	def __init__(self, *args, **kwargs):
		super(Subscribes, self).__init__(*args, **kwargs)

	def __repr__(self):
		return 'id: {}; ticker: {}; maxPrice: {};  minPrice: {};'.format(self.id, self.ticker, self.max_price, self.min_price)


class Tickers(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))

	def __init__(self, *args, **kwargs):
		super(Tickers, self).__init__(*args, **kwargs)
		
	def __repr__(self):
		return 'id: {}; ticker: {}; '.format(self.id, self.name)		
		