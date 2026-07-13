# app.py - Main Application
from flask import Flask, render_template, request, redirect, url_for, flash  # type: ignore
from database import init_db, add_student, get_all_students, get_student_by_name
from models import db, Student

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Initialize database
init_db(app)

@app.route('/')
def home():
    total_students = Student.query.filter_by(is_active=True).count()
    return render_template('home.html', total_students=total_students)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
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

@app.route('/student/<name>')
def student_profile(name):
    students = get_student_by_name(name)
    if students:
        return render_template('confirmation.html', student=students[0])
    else:
        flash('Student not found!', 'error')
        return redirect(url_for('register'))

@app.route('/students')
def students_list():
    all_students = get_all_students()
    return render_template('students_list.html', students=all_students)

@app.route('/search', methods=['GET'])
def search_students():
    search_term = request.args.get('q', '').strip()
    if search_term:
        students = get_student_by_name(search_term)
        return render_template('students_list.html', students=students, search_term=search_term)
    return redirect(url_for('students_list'))

def get_student_by_id(student_id):
    return Student.query.get(student_id)

@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
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
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    flash('Student deleted successfully!', 'success')

    return redirect(url_for('students_list'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)