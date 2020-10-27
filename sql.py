from flask import Flask
from datetime import datetime
from flask import render_template
from main import app
import pypyodbc
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

from flask import render_template, redirect, request

# creating connection Object which will contain SQL Server Connection
# connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.1.104,1433\LGEDSQL;Database=Mydatabase;uid=sa;pwd=12122012@Asif')  # Creating Cursor

SERVER = '172.16.1.104,1433\LGEDSQL'
DATABASE = 'Mydatabase'
DRIVER = 'SQL Server'
USERNAME = 'sa'
PASSWORD = '12122012@Asif'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()
# data = pd.read_sql_query("SELECT * FROM employee", connection)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"

# db.create_all()   //run this line only one to create db
# cursor1 = connection.cursor()
# cursor1.execute("SELECT * FROM employee")
# print(data)
# s = "<table style='border:1px solid red'>"
# for row in data:
#     s = s + "<tr>"
#     for x in row:
#         s = s + "<td>" + str(x) + "</td>"
#     s = s + "</tr>"
# connection.close()


@app.route('/')
@app.route('/home')
def home():
    return "<html><body>" + s + "</body></html>"


if __name__ == "__main__":
    app.run(debug=True)
