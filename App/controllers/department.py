# relevant controllers go here

# relevant controllers go here
from flask import Flask, request, jsonify
from App.models import Department, Program
from App.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
db.init_app(app)

# Controller methods

def create_department():
    data = request.get_json()
    new_department = Department(name=data['name'])
    db.session.add(new_department)
    db.session.commit()
    return {'message': 'Department created successfully', 'department': new_department.get_json()}, 201


def get_department(department_id):
    department = Department.query.get(department_id)
    if department:
        return department.get_json()
    else:
        return {'message': 'Department not found'}, 404


def update_department(department_id):
    department = Department.query.get(department_id)
    if department:
        data = request.get_json()
        department.name = data.get('name', department.name)

        db.session.commit()
        return {'message': 'Department updated successfully', 'department': department.get_json()}
    else:
        return {'message': 'Department not found'}, 404


def delete_department(department_id):
    department = Department.query.get(department_id)
    if department:
        db.session.delete(department)
        db.session.commit()
        return {'message': 'Department deleted successfully'}, 200
    else:
        return {'message': 'Department not found'}, 404


def get_department_programs(department_id):
    department = Department.query.get(department_id)
    if department:
        programs = [program.get_json() for program in department.programs]
        return {'programs': programs}
    else:
        return {'message': 'Department not found'}, 404
