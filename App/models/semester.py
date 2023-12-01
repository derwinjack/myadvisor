from App.database import db

class Semester(db.Model):
    __tablename__ = 'semesters'
    id = db.Column(db.Integer, primary_key=True)
    semester_title = db.Column(db.String(2))

    course_plan = db.relationship('CoursePlan', back_populates='sem_id')

    def __init__(self, sem_title):
        self.semester_title = sem_title