from app import app, db
from flask import Flask
from .models import TenderEntry, Transaction 
import random

@app.route('/')
def hello():

	transaction = Transaction(123, 10.00, "Sale", None)

	#Add the created entry to the table
	db.session.add(transaction)

	#transactionID = 55
	tenderType = "cash"
	amount = 75
 
	validTenderTypes = ["cash", "gift", "mastercard", "visa", "discover", "amex", "debit"]

	if tenderType.lower() not in validTenderTypes:
		return "Invalid tender type"

	#Create an entry in the tenderEntry table
	tenderEntry = TenderEntry(transaction.id, tenderType, amount)
	
	#Add the created entry to the table
	db.session.add(tenderEntry)
	
	#Save the changes in the database
	db.session.commit()

	return "ok"