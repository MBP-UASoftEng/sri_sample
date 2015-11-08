from app import db
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class TenderEntry (db.Model):

    __tablename__ = 'tenderEntry'

    id = db.Column(db.Integer, primary_key = True)
    transaction_id = db.Column(db.Integer, ForeignKey("transaction.id"), index = True, nullable = False)
    tenderType = db.Column(db.String)
    amount = db.Column(db.Integer)
    timestamp = db.Column(db.String)

    def __init__ (self, transactionID, tenderType, amount):
        self.transaction_id = transactionID
        self.tenderType = tenderType
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # For testing
    def __repr__ (self):
        return "tender entry Id: %s" % self.id


class Transaction (db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key = True)
    cashier_id = db.Column(db.Integer, ForeignKey("employee.id"), nullable = False)
    # cashier_id = db.Column(db.Integer, nullable = True) # Just for testing
    amount = db.Column(db.Float(precision=2, asdecimal = False, decimal_return_scale = None), nullable = False)
    transaction_type = db.Column(db.String, nullable = False)
    parent_id = db.Column(db.Integer, ForeignKey("transaction.id"), index = True, nullable = True)
    timestamp = db.Column(db.String, nullable = False)
    
    parent = db.relationship(lambda: Transaction, remote_side = id, backref = 'parent_transaction')
    tender_entries  =  db.relationship(lambda: TenderEntry, remote_side = id, backref = 'tender_transaction')

    def __init__ (self, cashier_id, amount, transaction_type, parent):
        self.cashier_id = cashier_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.parent = parent
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__ (self):
        return '<Transaction ID %r>' % self.id

class Employee (db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    employee_id = db.Column(db.Integer, unique = True, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    classification = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, nullable = False)
    manager_id = db.Column(db.Integer, ForeignKey("employee.id"), index = True, nullable = True)

    manager = relationship(lambda: Employee, remote_side = id, backref = 'underlings')

    def __init__ (self, first_name, last_name, active, classification, password, employee_id, manager):
        self.first_name = first_name
        self.last_name = last_name
        self.active = active
        self.password = password
        self.classification = classification
        self.employee_id = employee_id
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.manager = manager

    def __repr__ (self):
        return '<First Name %r>' % self.first_name