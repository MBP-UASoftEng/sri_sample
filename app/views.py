from app import app, db
from flask import Flask
from .models import Employee

@app.route('/')
def hello():

	first_name = "Harsha"
	last_name = "Bande"
	active = True
	password = "harsha123"

	#Create a entry in the employee table
	employee = Employee(first_name = first_name, last_name = last_name, active = active, password = password)
	
	#Add the created entry to the table
	db.session.add(employee)

	#Save the changes in the database
	db.session.commit()

	a = db.session.query(Employee).filter_by(first_name = "harsha").all()

	return str(len(a))