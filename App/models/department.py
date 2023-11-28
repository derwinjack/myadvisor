from App.models import User  
from App.database import db

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    prog = db.relationship('Program', back_populates='dept', uselist=False)


    def __init__(self, name):
        self.name = name

    
    def get_json(self):
        return{
            'Department ID: ' : self.id,
            'Department Name: ' : self.name,
        }