from .user import User 
from App.database import db

class Staff(User):

    
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(20))

    def __init__(self, staff_id, password, name, role):
        super().__init__(staff_id, password)
        self.id = staff_id
        self.name = name
        self.role = role

    def get_json(self):
        return{
            'Staff ID': self.id,
            'Name: ': self.name,
            'Role:' : self.role
        }

