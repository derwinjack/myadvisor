from .user import User 
from App.database import db

class Staff(User):
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(20))
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    dept = db.relationship('Department', back_populates='staff_member')

    def __init__(self, name, password, role, dept_id):
        super().__init__(name, password)
        self.id = super().id
        self.username = name
        self.role = role
        self.dept_id = dept_id

    def get_json(self):
        return{
            'Staff ID': self.id,
            'Name: ': self.username,
            'Role:' : self.role
        }

