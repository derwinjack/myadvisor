from App.database import db 
from flask import jsonify
from App.models import CourseHistory  

def create_course_history(course_id, student_id):
    new_course_history = CourseHistory(course_id=course_id, student_id=student_id)
    db.session.add(new_course_history)
    db.session.commit()
    return jsonify({'message': 'Course history created successfully'})

def get_course_history(course_history_id):
    course_history = CourseHistory.query.get(course_history_id)
    if course_history:
        return jsonify({'course_history': course_history.serialize()})
    else:
        return jsonify({'message': 'Course history not found'}), 404

def update_course_history(course_history_id, new_course_id, new_student_id):
    course_history = CourseHistory.query.get(course_history_id)
    if course_history:
        course_history.course_id = new_course_id
        course_history.student_id = new_student_id
        db.session.commit()
        return jsonify({'message': 'Course history updated successfully'})
    else:
        return jsonify({'message': 'Course history not found'}), 404

def delete_course_history(course_history_id):
    course_history = CourseHistory.query.get(course_history_id)
    if course_history:
        db.session.delete(course_history)
        db.session.commit()
        return jsonify({'message': 'Course history deleted successfully'})
    else:
        return jsonify({'message': 'Course history not found'}), 404
