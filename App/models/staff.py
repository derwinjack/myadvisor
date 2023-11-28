from .user import User 
from App.database import db

class Staff(User):
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(20))

    def __init__(self, name, password, role):
        super().__init__(name, password)
        self.id = super().id
        self.username = name
        self.role = role

    def get_json(self):
        return{
            'Staff ID': self.id,
            'Name: ': self.username,
            'Role:' : self.role
        }

