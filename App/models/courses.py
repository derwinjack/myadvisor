from App.database import db
from App.models import prerequisites
import json

class Course(db.Model):
    courseCode = db.Column(db.String(8), primary_key=True)
    courseTitle = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    credits = db.Column(db.Integer)
    grade = db.Column(db.Float)
    semester = db.Column(db.Integer)
    year = db.Column(db.Integer)
    prereq_id = db.Column(db.Integer, db.ForeignKey('prerequisites.id'))

    students = db.relationship('Student', backref='courses', lazy=True)
    programs = db.relationship('ProgramCourses', backref='courses', lazy=True)
    prerequisites = db.relationship('Prerequisites', backref='courses', lazy = True)
    course_plan = db.relationship('CoursePlan', backref='courses', lazy=True)

    
    def __init__(self, code, title, credits, grade, semester, year, complete, prereq):
        self.courseCode = code
        self.courseTitle = title
        self.credits = credits
        self.grade = grade
        self.semester = semester
        self.year = year
        self.complete = complete
        self.prereq_id = prereq
    
    def get_json(self):
        return{
            'Course Code:': self.courseCode,
            'Course Name: ': self.courseTitle,
            'Course Grade: ': self.grade,
            'No. of Credits: ': self.credits,
            'Semester: ': self.semester,
            'Year: ': self.year,
            'Completed?': self.complete,
            'Prerequisites: ': [prerequisites.get_json() for prerequisite in self.prerequisites]
        }