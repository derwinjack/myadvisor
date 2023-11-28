from abc import ABC, abstractmethod
from App.database import db

class CoursePlanStrategy(ABC):
    @abstractmethod
    def generateCoursePlan():
        pass

class CustomPlanStrategy(CoursePlanStrategy):
    def generateCoursePlan():
        return "Custom Course Plan Chosen"
    
class FastGradStrategy(CoursePlanStrategy):
    def generateCoursePlan():
        return "Fastest Graduation Course Plan Chosen"
    
class EasyCoursesStrategy(CoursePlanStrategy):
    def generateCoursePlan():
        return "Easiest Courses Course Plan Chosen"
    
class PrioritizeElectivesStrategy(CoursePlanStrategy):
    def generateCoursePlan():
        return "Prioritize Electives Course Plan Chosen"

class CoursePlan(db.Model):
    __tablename__='course_plans'
    id=db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer,  db.ForeignKey('student.id'), unique=True)
    
    student = db.relationship('Student', back_populates='course_plan', uselist=True)
    courses = db.relationship('Course', backref = 'course_plan', lazy=True)

    
    
    def __init__(self, plan_id, student_id, strategy: CoursePlanStrategy):
        self.id = plan_id
        self.studentId = student_id
        self._strategy = strategy
        
    def set_strategy(self, strategy: CoursePlanStrategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.generateCoursePlan()

    def get_json(self):
        return{
            'planId': self.id,
            'studentId': self.studentId,
            'Course Plan Strategy: ': self._strategy.__class__.__name__
        }