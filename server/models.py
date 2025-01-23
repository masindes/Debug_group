from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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