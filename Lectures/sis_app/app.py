# app.py - Main Application
from flask import Flask, render_template, request, redirect, url_for, flash, session  # type: ignore
from database import init_db, add_student, get_all_students, get_student_by_name, add_course, get_all_courses, edit_course, delete_course, enroll_student_in_course, get_enrollments, get_dept_list, add_dept, add_user, login_user
from models import Enrollment, db, Student, Course, Department, User
from auth import (
    login_required,
    guest_required,
    logout_user
)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Initialize database
init_db(app)

@app.route('/')
@login_required
def home():
    total_students = Student.query.filter_by(is_active=True).count()
    total_courses = Course.query.count()
    total_dept = Department.query.count()
    return render_template('home.html', total_students=total_students, total_courses=total_courses, dept_count = total_dept)

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/student/register', methods=['GET', 'POST'])
@login_required
def student_register():
    if request.method == 'POST':
        student_data = {
            'student_name': request.form.get('student_name', '').strip(),
            'registration_number': request.form.get('registration_number', '').strip(),
            'email': request.form.get('email', '').strip(),
            'programme': request.form.get('programme', '').strip()
        }
        
        if not all(student_data.values()):
            flash('All fields are required!', 'error')
            return render_template('register.html', form_data=student_data)
        
        success, message, student = add_student(student_data)
        
        if success:
            flash(message, 'success')
            student_name = student.student_name if student is not None else student_data['student_name']
            return redirect(url_for('student_profile', name=student_name))
        else:
            flash(message, 'error')
            return render_template('register.html', form_data=student_data)
    
    return render_template('register.html', form_data=None)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'username': request.form.get('username', '').strip(),
            'email': request.form.get('email', '').strip(),
            'full_name': request.form.get('full_name', '').strip(),
            'password': request.form.get('password', ''),
            'confirm_password': request.form.get('confirm_password', ''),
        }

        if not user_data['username'] or not user_data['email'] or not user_data['password']:
            flash('Username, email, and password are required.', 'error')
            return render_template('auth_register.html', form_data=user_data)

        if user_data['password'] != user_data['confirm_password']:
            flash('Passwords do not match.', 'error')
            return render_template('auth_register.html', form_data=user_data)

        success, message, _ = add_user(user_data)

        if success:
            flash(message, 'success')
            return redirect(url_for('login'))

        flash(message, 'error')
        return render_template('auth_register.html', form_data=user_data)

    return render_template('auth_register.html', form_data=None)

@app.route('/student/<name>')
@login_required

def student_profile(name):
    students = get_student_by_name(name)
    if students:
        return render_template('confirmation.html', student=students[0])
    else:
        flash('Student not found!', 'error')
        return redirect(url_for('student_register'))

@app.route('/students')
@login_required

def students_list():
    all_students = get_all_students()
    return render_template('students_list.html', students=all_students)

@app.route('/search', methods=['GET'])
@login_required

def search_students():
    search_term = request.args.get('q', '').strip()
    if search_term:
        students = get_student_by_name(search_term)
        return render_template('students_list.html', students=students, search_term=search_term)
    return redirect(url_for('students_list'))

def get_student_by_id(student_id):
    return Student.query.get(student_id)

@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required

def edit_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        student.student_name = request.form['student_name']
        student.registration_number = request.form['registration_number']
        student.email = request.form['email']
        student.programme = request.form['programme']

        db.session.commit()

        flash('Student updated successfully!', 'success')

        return redirect(url_for('students_list'))

    return render_template(
        'edit_student.html',
        student=student
    )


@app.route('/student/delete/<int:student_id>', methods=['POST'])
@login_required

def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    flash('Student deleted successfully!', 'success')

    return redirect(url_for('students_list'))




# Add course
@app.route('/registercourse', methods=['GET', 'POST'])
@login_required

def registercourse():
    if request.method == 'POST':
        course_data = {
            'course_name': request.form.get('course_name', '').strip(),
            'course_code': request.form.get('course_code', '').strip(),
            'course_weight': request.form.get('course_weight', '').strip(),
        }
        
        if not all(course_data.values()):
            flash('All fields are required!', 'error')
            return render_template('add_course.html', form_data=course_data)
        
        success, message, course = add_course(course_data)
        
        if success:
            flash(message, 'success')
            course_name = course.course_name if course is not None else course_data['course_name']
            return redirect(url_for('course_profile', name=course_name))
        else:
            flash(message, 'error')
            return render_template('add_course.html', form_data=course_data)
    
    return render_template('add_course.html', form_data=None)

# Edit course
@app.route('/course/edit/<int:course_id>', methods=['GET', 'POST'])
@login_required

def edit_course_route(course_id):
    course = Course.query.get_or_404(course_id)

    if request.method == 'POST':
        course.course_name = request.form['course_name']
        course.course_code = request.form['course_code']
        course.course_weight = request.form['course_weight']

        db.session.commit()

        flash('Course updated successfully!', 'success')

        return redirect(url_for('course_list'))

    return render_template(
        'edit_course.html',
        course=course
    )


@app.route('/course_profile/<name>')
@login_required

def course_profile(name):
    course = Course.query.filter_by(course_name=name).first()
    if course:
        return render_template('course_success.html', course=course)
    else:
        flash('Course not found!', 'error')
        return redirect(url_for('registercourse'))
    


@app.route('/courses')
@login_required

def course_list():
    courses = get_all_courses()
   
    return render_template('course_list.html', courses=courses)


@app.route('/course/delete/<int:course_id>', methods=['POST'])
@login_required

def delete_course_route(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    flash('Course deleted successfully!', 'success')

    return redirect(url_for('course_list'))


# Student enrollment route
@app.route('/enroll', methods=['GET', 'POST'])
@login_required

def enroll_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')

        success, message = enroll_student_in_course(student_id, course_id)

        if success:
            flash(message, 'success')
            return redirect(url_for('enrollments_list'))
        else:
            flash(message, 'error')

    students = get_all_students()
    courses = get_all_courses()
    return render_template('enroll_student.html', students=students, courses=courses)


# Enrollment list route
@app.route('/enrollments')
@login_required

def enrollments_list():
    enrollments = Enrollment.query.all()
    return render_template('enrollments_list.html', enrollments=enrollments)


# Department routes
@app.route('/departments')
@login_required
def dept_list():
    departments = Department.query.all()
    return render_template('dept_list.html', departments = departments)


@app.route('/adddept', methods=['GET', 'POST'])
@login_required
def adddept():
    if request.method == 'POST':
        dept_data = {
            'dept_name': request.form.get('dept_name', '').strip(),
            'dept_code': request.form.get('dept_code', '').strip(),
        }
        
        if not all(dept_data.values()):
            flash('All fields are required!', 'error')
            return render_template('add_dept.html', form_data=dept_data)
        
        add_dept(dept_data)
      
    return render_template('add_dept.html', form_data=None)

@app.route("/login", methods=["GET", "POST"])
@guest_required
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Username and password are required.", "error")
            return render_template("login.html")

        success, result = login_user(username, password)

        if success and isinstance(result, User):
            session["user_id"] = result.id
            session["username"] = result.username

            flash("Login successful.", "success")

            return redirect(url_for("home"))

        flash(result if isinstance(result, str) else "Login failed.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.","success")

    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)