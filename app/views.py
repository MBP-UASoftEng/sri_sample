from app import app, db
from flask import Flask
from .models import TenderEntry

@app.route('/')
def hello():

	transactionID = 55
	tenderType = "cash"
	amount = 64.67
	timestamp = "2/12/2015"
	
	validTenderTypes = ["cash", "gift", "mastercard", "visa", "discover", "amex", "debit"]

	if tenderType.lower() not in validTenderTypes:
		return "Invalid tender type"

	#Create an entry in the tenderEntry table
	tenderEntry = TenderEntry(recordID, transactionID, tenderType, amount, timestamp)
	
	#Add the created entry to the table
	db.session.add(tenderEntry)

	#Save the changes in the database
	db.session.commit()

	a = db.session.query(tenderEntry).filter_by(transactionID = 55).all()

	return str(len(a))
