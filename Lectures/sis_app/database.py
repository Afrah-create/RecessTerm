# database.py - Database Operations
from flask_sqlalchemy import SQLAlchemy  # pyright: ignore[reportMissingImports]
from models import db, Student

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("✅ Database initialized successfully!")
        
        if Student.query.count() == 0:
            add_sample_data()

def add_sample_data():
    sample_students = [
        Student(
            student_name='Awongo Fahadi Rashid',
            registration_number='24/U/22771',
            email='awongo.fahadi@mak.ac.ug',
            programme='Computer Science'
        ),
        Student(
            student_name='Ajua Gloria',
            registration_number='24/U/25772',
            email='ajua.gloria@mak.ac.ug',
            programme='Information Technology'
        )
    ]
    
    for student in sample_students:
        db.session.add(student)
    db.session.commit()
    print("📚 Sample students added successfully!")

def get_all_students():
    return Student.query.filter_by(is_active=True).all()

def get_student_by_name(name):
    return Student.query.filter(
        Student.student_name.contains(name),
        Student.is_active == True
    ).all()

def get_student_by_registration(registration_number):
    return Student.query.filter_by(registration_number=registration_number).first()

def add_student(student_data):
    try:
        existing = get_student_by_registration(student_data['registration_number'])
        if existing:
            return False, "Registration number already exists!", None
        
        existing_email = Student.query.filter_by(email=student_data['email']).first()
        if existing_email:
            return False, "Email already registered!", None
        
        new_student = Student(
            student_name=student_data['student_name'],
            registration_number=student_data['registration_number'],
            email=student_data['email'],
            programme=student_data['programme']
        )
        
        db.session.add(new_student)
        db.session.commit()
        return True, "Student registered successfully!", new_student
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}", None
    
def update_student(student_id, updated_data):
    try:
        student = Student.query.get(student_id)
        if not student:
            return False, "Student not found!"
        
        if 'student_name' in updated_data:
            student.student_name = updated_data['student_name']
        if 'registration_number' in updated_data:
            existing = get_student_by_registration(updated_data['registration_number'])
            if existing and existing.id != student_id:
                return False, "Registration number already exists!"
            student.registration_number = updated_data['registration_number']
        if 'email' in updated_data:
            existing_email = Student.query.filter_by(email=updated_data['email']).first()
            if existing_email and existing_email.id != student_id:
                return False, "Email already registered!"
            student.email = updated_data['email']
        if 'programme' in updated_data:
            student.programme = updated_data['programme']
        
        db.session.commit()
        return True, "Student updated successfully!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
    


def soft_delete_student(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return False, "Student not found!"
        
        student.is_active = False
        db.session.commit()
        return True, "Student deleted successfully!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
    

def permanent_delete_student(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return False, "Student not found!"
        try:
            db.session.delete(student)
            db.session.commit()
            return True, "Student permanently deleted successfully!"
        except Exception as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"