from app import db
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class TenderEntry (db.Model):

    __tablename__ = 'tenderentry'

    recordID = db.Column(db.Integer, primary_key=True)
    transactionID = db.Column(db.Integer, ForeignKey ("transaction.id"), index = True, nullable = True)
    tenderType = db.Column(db.String)
    amount = db.Column(db.Integer)
    timestamp = db.Column(db.String)

    transaction = relationship (lambda: transaction, remote_side = id)

    def __init__ (recordID, transactionID, tenderType, amount):
        self.recordID = recordID
        self.transactionID = transactionID
        self.tenderType = tenderType
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # For testing
    def __repr__ (self):
        return "transactionID Id: %s" % transactionID

