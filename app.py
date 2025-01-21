from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 
migrate = Migrate(app, db)

class Safaricom_employees(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    department = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    job_group = db.Column(db.String, nullable=False)
    branch = db.Column(db.String, nullable=False)   
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'),nullable=False) 
    employer = db.relationship('Safaricom')

    def __repr__(self):
        return f'employee name: {self.name}, department: {self.department}, salary: {self.salary}, job_group: {self.job_group}, branch: {self.branch}'

class Safaricom(db.Model):
    __tablename__ = 'employer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)   
    branch = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'employee name: {self.name}, branch: {self.branch}' 
    
    if __name__ == '__main__':
        app.run(debug=True, port=5555)
    