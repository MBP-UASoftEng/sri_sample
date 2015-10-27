from app import app, db
from flask import Flask
from .models import TenderEntry, Transaction 
import random

@app.route('/')
def hello():

	transaction = Transaction(123, 10, "Sale", None)

	#Add the created entry to the table
	db.session.add(transaction)

	#transactionID = 55
	tenderType = "cash"
	amount = 64.67
	timestamp = "2/12/2015"

	validTenderTypes = ["cash", "gift", "mastercard", "visa", "discover", "amex", "debit"]

	if tenderType.lower() not in validTenderTypes:
		return "Invalid tender type"

	#Create an entry in the tenderEntry table
	tenderEntry = TenderEntry(transaction, tenderType, amount)
	
	#Add the created entry to the table
	db.session.add(tenderEntry)

	#Save the changes in the database
	db.session.commit()

	return str(len(a))