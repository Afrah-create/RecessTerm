# database.py - Database Operations
from flask_sqlalchemy import SQLAlchemy  # pyright: ignore[reportMissingImports]
from models import Enrollment, db, Student, Course, Department

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
    

def add_course(course_data):
    try:
        existing_courses = Course.query.filter_by(course_code = course_data['course_code']).first()
        if existing_courses:
            return False, "Course Code already Exists", None
        new_course = Course(
            course_name = course_data['course_name'],
            course_code = course_data['course_code'],
            course_weight = course_data['course_weight']
        )

        db.session.add(new_course)
        db.session.commit()

        return True, 'Course added successfully', new_course
    except Exception as e:
        db.session.rollback()
        return False, str(e), None
    
def get_all_courses():
    return Course.query.all()

def edit_course(course_id, updated_data):
    try:
        course = Course.query.get(course_id)
        if not course:
            return False, "Course not found!"
        
        if 'course_name' in updated_data:
            course.course_name = updated_data['course_name']
        if 'course_code' in updated_data:
            existing = Course.query.filter_by(course_code=updated_data['course_code']).first()
            if existing and existing.id != course_id:
                return False, "Course code already exists!"
            course.course_code = updated_data['course_code']
        if 'course_weight' in updated_data:
            course.course_weight = updated_data['course_weight']
        
        db.session.commit()
        return True, "Course updated successfully!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
    

def delete_course(course_id):
    try:
        course = Course.query.get(course_id)
        if not course:
            return False, "Course not found!"
        db.session.delete(course)
        db.session.commit()
        return True, "Course successfully Deleted!"
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
    
def enroll_student_in_course(student_id, course_id):
    try:
        student = Student.query.get(student_id)
        course = Course.query.get(course_id)
        
        if not student or not course:
            return False, "Student or Course not found!"
        
        existing_enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
        if existing_enrollment:
            return False, "Student is already enrolled in this course!"
        
        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        
        return True, "Student enrolled successfully!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"
    

def get_enrollments():
    return Enrollment.query.all()



def add_dept(dept_data):
    try:
        existing_depts = Department.query.all()
        if existing_depts:
            return False, "Department already exists"
        new_dept = Department(
            dept_name = dept_data['dept_name'],
            dept_code = dept_data['dept_code']

        )

        db.session.add(new_dept)
        db.session.commit()
        return True, "Department added successfully"
    except Exception as e:
        db.session.rollback()
        return False, str(e), None
    
def get_dept_list():
    return Department.query.all()