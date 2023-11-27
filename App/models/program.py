from App.database import db
from App.models import department

class Program(db.Model):
    __tablename__ = 'program'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    core_credits = db.Column(db.Integer)
    elective_credits = db.Column(db.Integer)
    foun_credits = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    
    department = db.relationship('Department', back_populates='program', overlaps='program')
    students = db.relationship('Student', back_populates='program', lazy=True)
    courses = db.relationship('ProgramCourses', backref='program', lazy=True)


    def __init__(self, name, core, elect, foun):
       self.name = name
       self.core_credits = core
       self.elective_credits = elect
       self.foun_credits = foun


    def get_json(self):
        return{
            'Program ID:': self.id,
            'Department ID: ': self.department_id,
            'Program Name: ': self.name,
            'Core Credits: ': self.core_credits,
            'Elective Credits ': self.elective_credits,
            'Foundation Credits: ': self.foun_credits
        }
       