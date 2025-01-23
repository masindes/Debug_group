from flask import Flask, jsonify, request
from models import db, Safaricom, Safaricom_employees
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Configuring the app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safaricom.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Create tables in the database (done through migrations)
# This is no longer needed as `flask db` commands will handle it

# CRUD Routes

# Create an employee
@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('department'):
        return jsonify({'message': 'Missing fields'}), 400
    
    employee = Safaricom_employees(
        name=data['name'],
        department=data['department'],
        salary=data['salary'],
        job_group=data['job_group'],
        branch=data['branch'],
        employer_id=data['employer_id']
    )
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee created', 'id': employee.id}), 201

# Get all employees
@app.route('/employee', methods=['GET'])
def get_employees():
    employees = Safaricom_employees.query.all()
    return jsonify([{'id': e.id, 'name': e.name} for e in employees])

# Get employee by ID
@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Safaricom_employees.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify({
        'id': employee.id,
        'name': employee.name,
        'department': employee.department,
        'salary': employee.salary,
        'job_group': employee.job_group,
        'branch': employee.branch,
        'employer_id': employee.employer_id
    })

# Update an employee
@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Safaricom_employees.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    
    data = request.get_json()
    employee.name = data.get('name', employee.name)
    employee.department = data.get('department', employee.department)
    employee.salary = data.get('salary', employee.salary)
    employee.job_group = data.get('job_group', employee.job_group)
    employee.branch = data.get('branch', employee.branch)
    
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

# Delete an employee
@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Safaricom_employees.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)