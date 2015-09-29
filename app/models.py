from app import db
import datetime

class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    active = db.Column(db.Boolean)
    password = db.Column(db.String)
    timestamp = db.Column(db.String)

    def __init__(self, first_name, last_name, active, password):
        self.first_name = first_name
        self.last_name = last_name
        self.active = active
        self.password = password
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<E-mail %r>' % self.first_name