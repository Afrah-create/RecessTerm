from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    """
    Displays the application's public home page.
    """
    return render_template('landing.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles displaying the login page (GET) and processing 
    the incoming authentication form data (POST).
    """
    if request.method == 'POST':
        # Retrieve form parameters submitted by the user
        username = request.form.get('username')
        password = request.form.get('password')
        

        if username == "Afrah" and password == "afrah123":
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Please try again.", 401

    # If request method is GET, simply display the login screen
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """
    Displays the application's internal home dashboard space after 
    successful authentication. Safely receives GET redirect requests.
    """
    return render_template('dashboard.html')


# --- Server Entrypoint ---

if __name__ == '__main__':
    # Starts the application server with hot-reload debugging active
    app.run(debug=True)