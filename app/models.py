from app import db
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Employee(db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    employee_id = db.Column(db.Integer, unique=True, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    classification = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, nullable = False)
    manager_id = db.Column(db.Integer, ForeignKey("employee.id"), index = True, nullable = True)

    manager = relationship(lambda: Employee, remote_side=id, backref='underlings')

    def __init__(self, first_name, last_name, active, classification, password, employee_id, manager):
        self.first_name = first_name
        self.last_name = last_name
        self.active = active
        self.password = password
        self.classification = classification
        self.employee_id = employee_id
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.manager = manager

    def __repr__(self):
        return '<First Name %r>' % self.first_name