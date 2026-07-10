# Page to display the home page of the application
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__) # __name__ is a special variable in Python that represents the name of the current module. When you run a Python script, __name__ is set to "__main__". When you import a module, __name__ is set to the module's name. In this case, it helps Flask determine the root path of the application.


# Decorator to define a route for the home page of the application. When a user visits 
# the root URL ('/'), the home() function will be called, and it will render the 
# 'home.html' template.
@app.route('/')
def home():
    return render_template('front-end/home.html')  # This line renders the 'home.html' template as the response for the home page.


@app.route('/about')
def about():
    return render_template('front-end/about.html')  # This line renders the 'about.html' template as the response for the about page.

@app.route('/contact')
def contact():
    return render_template('front-end/contact.html')  # This line renders the 'contact.html' template as the response for the contact page.


# To ensure the server runs only when the script is executed directly (not when imported
#  as a module), we use the following conditional statement. If the script is run directly, 
# the Flask application will start in debug mode, which provides helpful error messages 
# and automatically reloads the server when code changes are detected.





# Dynamic routing allows you to capture values from the URL and pass them as parameters to your view functions. In Flask, you can define dynamic routes by using angle brackets (<>) in the route definition. For example, if you want to create a route that displays a user's profile based on their username, you can define a dynamic route like this:
@app.route('/user/<username>')
def user_profile(username):
    return f'<h1>User Profile</h1><p>Welcome, {username}!</p>'  # This line returns a simple HTML response that includes the captured username from the URL.



# Dynamic route to display my story based on the story ID provided in the URL. 
# The <story_id> part of the route captures the value from the URL and passes it as an 
# argument to the myStory function.
@app.route('/mystory/<story_id>')
def myStory(story_id):
    story_id = 'My name is Afrah'
    return f'<p>Story ID: {story_id}</p>'  # This line returns a simple HTML response that includes the captured story ID from the URL.

@app.route('/profile/<string: username>/<int: user_id>')
def profile(username, user_id):
    return render_template('profile.html', username='Afrah', user_id=123)  # This line renders the 'profile.html' template as the response for the profile page.

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application in debug mode.

# Routing refers to the process of defining URL patterns and associating them with 
# specific functions or views in a web application. In Flask, routing is achieved using 
# decorators like @app.route(). When a user visits a specific URL, Flask matches the URL 
# pattern to the corresponding route and executes the associated function, returning the 
# appropriate response (e.g., HTML page, JSON data, etc.).