from app import app, db
from flask import Flask
from .models import TransactionEntry
import random

@app.route('/')
def hello():

	transaction_id = None

	product_id = 45
	price = "%.2f" % random.uniform(0.01, 100.00)
	quantity = 5

	#creates an entry in the Transaction Entry table
	transaction_entry = TransactionEntry(transaction_id = transaction_id, product_id = product_id, price = price, quantity = quantity)

	db.session.add(transaction_entry)

	db.session.commit()

	return "Entry added to db successfully."
