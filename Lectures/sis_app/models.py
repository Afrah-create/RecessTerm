# models.py - Database Models
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy  # pyright: ignore[reportMissingImports]

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    registration_number = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    programme = db.Column(db.String(100), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Student {self.student_name} - {self.registration_number}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_name': self.student_name,
            'registration_number': self.registration_number,
            'email': self.email,
            'programme': self.programme,
            'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            'is_active': self.is_active
        }


# Courses
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key = True)
    course_name = db.Column(db.String(100), nullable = False)
    course_code = db.Column(db.String(50), unique = True, nullable = False)
    course_weight = db.Column(db.Integer, nullable = True)
    is_active = db.Column(db.Boolean, default = True)

    def __repr__(self):
        return f'<Course {self.course_weight} - {self.course_code}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'course_code': self.course_code,
            'course_weight': self.course_weight
        }
    


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))
    
    def __repr__(self):
        return f'<Enrollment Student ID: {self.student_id}, Course ID: {self.course_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date.strftime('%Y-%m-%d %H:%M:%S')
        }
    
class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)
    dept_code = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f'<Department Id: {self.dept_code}, Department Name: {self.dept_name}'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'dept_name' : self.dept_name,
            'dept_code' : self.dept_code

        }