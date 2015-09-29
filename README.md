Simple Flask app to add a person to a database

To get this thing set up:
1) Make sure python is installed on the computer
2) Make sure pip is installed on the computer. Pip is used to install python libraries from the command line
3) Make sure postgresql is installed on the computer and create a database called test

In the root directory run pip install -r requirements.txt to install all the necessary python libraries

While in the root directory, go to the python compiler by typing "python"

In the compiler type "from app import db" and then "db.create_all()" to create the db table

To run the website, in the root directory type "python run.py" to get the web server up and running

Go to localhost:5000 to see the website