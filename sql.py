from flask import Flask
from datetime import datetime
from flask import render_template
from main import app
import pypyodbc
from datetime import datetime

from flask import render_template, redirect, request

# creating connection Object which will contain SQL Server Connection
connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.1.104,1433\LGEDSQL;Database=Mydatabase;uid=sa;pwd=12122012@Asif')  # Creating Cursor

cursor = connection.cursor()
cursor.execute("SELECT * FROM employee")
s = "<table style='border:1px solid red'>"
for row in cursor:
    s = s + "<tr>"
    for x in row:
        s = s + "<td>" + str(x) + "</td>"
    s = s + "</tr>"
connection.close()


@app.route('/')
@app.route('/home')
def home():
    return "<html><body>" + s + "</body></html>"

if __name__ == "__main__":
    app.run(debug=True)