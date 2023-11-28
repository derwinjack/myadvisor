from App.database import db
class Prerequisites(db.Model):

    prereq_code = db.Column(db.String, primary_key=True)
    prereq_name = db.Column(db.String(8), nullable=False)
    courseCode = db.Column(db.String(8), db.ForeignKey('courses.id'))
    

    def __init__(self, prereq_code, nameofCourse):
        self.prereq_courseCode = prereq_code
        self.courseName = nameofCourse

    def get_json(self):
        return{
            'Prerequisite Code': self.prereq_courseCode,
            'Prerequisite Title':self.prereq_name
        } 