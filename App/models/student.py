from App.models import User  
from App.database import db

class Student(User):
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    gpa = db.Column(db.Float) 
    program_id = db.Column(db.ForeignKey('programs.id')) 
    
    prog = db.relationship('Program', back_populates='stu')
    
    course_plan = db.relationship('CoursePlan', back_populates='student', uselist=False)


    def __init__(self, name, password, program_id):
        super().__init__(name, password)
        self.id = super().id
        self.name = name
        self.gpa= 0.0
        self.program_id = program_id

    def get_json(self):
        return{'Student ID': self.id,
            'Name': self.name,
            'Program' : self.program_id,
            'GPA: ' : self.gpa
            
        }

