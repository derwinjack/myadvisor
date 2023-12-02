from flask import jsonify, request
from App.models import Program
from App.database import db
from App.models.course import Course

def create_program(name, core_credits, elective_credits, foun_credits, department_id):
    newProgram = Program(name, core_credits, elective_credits, foun_credits, department_id)
    db.session.add(newProgram)
    print("Program successfully created")
    db.session.commit()
    return newProgram

def update_program(program_id):
    program = Program.query.get(program_id)
    if program:
        data = request.get_json()
        program.name = data.get('name', program.name)
        program.core_credits = data.get('core_credits', program.core_credits)
        program.elective_credits = data.get('elective_credits', program.elective_credits)
        program.foun_credits = data.get('foun_credits', program.foun_credits)
        program.department_id = data.get('department_id', program.department_id)

        db.session.commit()
        return jsonify({'message': 'Program updated successfully', 'program': program.get_json()})
    else:
        return jsonify({'message': 'Program not found'}), 404
    

def get_program_by_name(programName):
    return Program.query.filter_by(name=programName).first()

def get_program_by_id(programId):
    return Program.query.filter_by(id=programId).first()

def get_level1_credits(programID):
    program = get_program_by_id(programID)
    return program.level1_credits if program else 0

def get_level1_courses(programID):
    program = get_program_by_id(programID)
    courses = program.str_level1_courses()
    return courses if program else []

def get_core_credits(programID):
    program = get_program_by_id(programID)
    return program.core_credits if program else 0

def get_core_courses(programID):
    program = get_program_by_id(programID)
    courses = program.str_core_courses()
    return courses if program else []

def get_elective_credits(programID):
    program = get_program_by_id(programID)
    return program.elective_credits if program else 0

def get_elective_courses(programID):
    program = get_program_by_id(programID)
    courses = program.str_elective_courses()
    return courses if program else []

def get_foun_credits(programID):
    program = get_program_by_id(programID)
    return program.foun_credits if program else 0

def get_foun_courses(programID):
    program = get_program_by_id(programID)
    courses = program.str_foun_courses()
    return courses if program else []

def get_all_courses(programID):
    core_courses = get_core_courses(programID)
    elective_courses = get_elective_courses(programID)
    foun_courses = get_foun_courses(programID)

    all = core_courses + elective_courses + foun_courses
    return all


def programCourses_SortedbyHighestCredits(program_id):
    # Assuming you have a Course model with a program_id field
    program_courses = Course.query.filter_by(program_id=program_id).all()

    # Sort the courses by credits in descending order
    sorted_courses = sorted(program_courses, key=lambda x: x.credits, reverse=True)

    return sorted_courses

def programCourses_SortedbyHighestRating(program_id):
    # Assuming you have a Course model with a program_id field
    program_courses = Course.query.filter_by(program_id=program_id).all()

    # Sort the courses by credits in descending order
    sorted_courses = sorted(program_courses, key=lambda x: x.rating, reverse=True)

    return sorted_courses

def programCourses_SortedbyElectivesFirst(program_id):
    # Assuming you have a Course model with a program_id field and a type field for course type
    program_courses = Course.query.filter_by(program_id=program_id).all()

    # Sort the courses by type (electives first) and then by credits in descending order
    sorted_courses = sorted(program_courses, key=lambda x: (x.type != 'elec', x.credits), reverse=True)

    return sorted_courses


