from app import app, db
from flask import Flask
from .models import Employee
import random

@app.route('/')
def hello():

	first_name1 = "Manager".lower()
	last_name1 = "Manager".lower()
	active1 = True;
	password1 = "harsha1233"
	classification1 = "manager".lower().replace(" ", "")
	unique1 = False
	employee_id1 = None
	while not unique1:
		emp_id = random.randint(100000, 999999)
		exists = Employee.query.filter_by(employee_id = emp_id).all()
		if len(exists) == 0:
			unique1 = True
			employee_id1 = emp_id

	manager = Employee(first_name = first_name1, last_name = last_name1, active = active1, classification = classification1, password = password1, employee_id = employee_id1, manager = None)

	#Add the created entry to the table
	db.session.add(manager)

	first_name = "Harsha".lower()
	last_name = "Bande".lower()
	active = True
	password = "harsha123"

	classifications = ["generalmanager", "shiftmanager", "cashier"]

	classification = "Cashier".lower().replace(" ", "")

	if classification not in classifications:
		return "Incorrect classification"

	unique = False
	employee_id = None
	while not unique:
		emp_id = random.randint(100000, 999999)
		exists = Employee.query.filter_by(employee_id = emp_id).all()
		if len(exists) == 0:
			unique = True
			employee_id = emp_id

	#Create a entry in the employee table
	employee = Employee(first_name = first_name, last_name = last_name, active = active, classification = classification, password = password, employee_id = employee_id, manager = manager.id)
	
	#Add the created entry to the table
	db.session.add(employee)

	#Save the changes in the database
	db.session.commit()

	a = Employee.query.filter_by(first_name = "harsha").all()

	return str(len(a))

@app.route('/lookup', method=['GET'])
def lookup(lookup_code):
	 product = db.session.query(Product).filter_by(ItemLookupCode = lookup_code).first()
	 

