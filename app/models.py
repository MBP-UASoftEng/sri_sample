from app import db
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class TransactionEntry(db.Model):

	__tablename__ = 'transaction_entry'

	id = db.Column(db.Integer, primary_key=True)

	#transaction_id = db.Column(db.integer, ForeignKey("transaction.id"), nullable=False)
	transaction_id = db.Column(db.Integer, nullable=True)
	product_id = db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float(precision=2,asdecimal=False, decimal_return_scale=None), nullable=False)
	quantity = db.Column(db.Integer, nullable=False)


	def __init__(self, transaction_id, product_id, price, quantity):
    		self.transaction_id = transaction_id
    		self.product_id = product_id
    		self.price = price
    		self.quantity = quantity

	def __repr__(self):
	    return '<Transaction Entry ID %r>' % self.id
