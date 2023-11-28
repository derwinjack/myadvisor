from flask import request
from App.models import Course, Prerequisites
from App.controllers.prerequistes import (create_prereq, get_all_prerequisites)
from App.database import db
import json, csv

#def createPrerequistes(prereqs, courseName):
 ##      prereq_course = Course.query.filter_by(courseCode=prereq_code).first()
        
   #     if prereq_course:
    #        create_prereq(prereq_code,courseName) 

def create_course():
    data = request.get_json()
    prereq_id = data.get('prereq_id')  # assuming prereq_id is provided in the request data
    prereq = Prerequisites.query.get(prereq_id) if prereq_id else None

    new_course = Course(
        code=data['courseCode'],
        title =data['courseTitle'],
        credits=data['credits'],
        grade=data['grade'],
        semester=data['semester'],
        year=data['year'],
        complete=data['complete'],
        prereq=prereq
    )
    
    db.session.add(new_course)
    db.session.commit()
    return {'message': 'Course created successfully', 'course': new_course.get_json()}, 201


def createCoursesfromFile(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                courseCode = row["courseCode"]
                courseTitle = row["courseTitle"]
                credits = int(row["numCredits"])
                rating = int(row["ratings"])
                grade=row['grade']
                semester=row['semester']
                year=int (row['year'])
                complete= row['complete']
                prereq= row["preReqs"].split(',')

                create_course(courseCode, courseTitle, credits,rating, grade, semester, year, complete, prereq)
                
    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
    print("Courses added successfully.")
    
def get_course_by_courseCode(code):
    return Course.query.filter_by(courseCode=code).first()

def courses_Sorted_byRating():
    courses =  Course.query.order_by(Course.rating.asc()).all()
    codes = []

    for c in courses:
        codes.append(c.courseCode)
    
    return codes

def courses_Sorted_byRating_Objects():
    return Course.query.order_by(Course.rating.asc()).all()
    

def get_prerequisites(code):
    course = get_course_by_courseCode(code)
    prereqs = get_all_prerequisites(course.courseName)
    return prereqs

def get_credits(code):
    course = get_course_by_courseCode(code)
    return course.credits if course else 0

def get_ratings(code):
    course = get_course_by_courseCode(code)
    return course.rating if course else 0


def update_course(course_code):
    course = Course.query.get(course_code)
    if course:
        data = request.get_json()
        prereq_id = data.get('prereq_id')
        prereq = Prerequisites.query.get(prereq_id) if prereq_id else None

        course.title = data.get('courseTitle', course.title)
        course.credits = data.get('credits', course.credits)
        course.grade = data.get('grade', course.grade)
        course.semester = data.get('semester', course.semester)
        course.year = data.get('year', course.year)
        course.complete = data.get('complete', course.complete)
        course.prereq = prereq

        db.session.commit()
        return {'message': 'Course updated successfully', 'course': course.get_json()}
    else:
        return {'message': 'Course not found'}, 404


def delete_course(course_code):
    course = Course.query.get(course_code)
    if course:
        db.session.delete(course)
        db.session.commit()
        return {'message': 'Course deleted successfully'}, 200
    else:
        return {'message': 'Course not found'}, 404




