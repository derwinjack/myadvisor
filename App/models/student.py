from App.models import User  
from App.database import db

class Student(User):
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    gpa = db.Column(db.Float)
    program_id = db.Column(db.ForeignKey('program.id')) 
    
    department = db.relationship('Department', backref='student', lazy=True)
    associated_program = db.relationship('Program', back_populates='student', overlaps="program")
    course_history = db.relationship('Course', back_populates='student', lazy=True)
    course_plan = db.relationship('CoursePlan', back_populates='student')


    def __init__(self, username, password, name, program_id):
        super().__init__(username, password)
        self.id = username
        self.name = name
        self.program_id = program_id

    def get_json(self):
        return{'Student ID': self.id,
            'Name': self.name,
            'Program' : self.program_id,
            'GPA: ' : self.gpa
            
        }

