from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


@app.route('/case/<case_number>')
def get_cases(case_number):
    
    return

@app.route('/docket/<complete_case_number>')
def get_docket(complete_case_number):
    return

@app.route('/sentence/<complete_case_number>')
def get_sentence(complete_case_number):
    return

@app.route('sentence/incarceration/<complete_case_number>')
def get_incarceration(complete_case_number):
    return

@app.route('sentence/probation/<complete_case_number>')
def get_probation(complete_case_number):
    return

@app.route('sentence/fine/<complete_case_number>')
def get_fine(complete_case_number):
    return

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"