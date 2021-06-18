from flask import Flask, render_template, request, make_response, flash, redirect
from flask.helpers import url_for
import os

# Make this app is a flask app
app = Flask(__name__)

# Set a secret key to use flashed messages
app.secret_key = os.urandom(32)

# Cookies max age fixed
DAY = 60 * 60 * 24

# Unities functions
def init_cookines(response_page, days_number):
    response = make_response(render_template(response_page))
    response.set_cookie("username", "", max_age= days_number * DAY)
    response.set_cookie("password", "", max_age= days_number * DAY)

    return response


# Homepage logic
@app.route("/", methods=["GET", "POST"])
def index():

    # If cookies are None in GET request
    if request.cookies.get("username") == None or request.cookies.get("password") == None:
        
        # Make a response, initialize cookies and reload the page
        return init_cookines("index.html", 5), 302

    # Cookies data
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    
    # Else render the homepage
    return render_template("index.html", username=username, password=password)

# Login page logic
@app.route("/login", methods=["GET", "POST"])
def login():

    # If cookies are None in GET request
    if request.cookies.get("username") == None or request.cookies.get("password") == None:
        
        # Make a response, initialize cookies and reload the page
        return init_cookines("login.html", 5), 302
    
    if request.method == "POST":

        # Get form data from in register page
        current_username = request.form.get("username").strip()
        current_password = request.form.get("password")

        """
        - To validate data we have two scenarios here:
            1- one field is empty or both or both of fields 
            2- one field has increct data entry or both of fields 
        """

        # Validate data emptiness
        if len(current_username) > 0 or len(current_password) > 0:

            # Validate data correctness
            # Cookies data
            cookie_username = request.cookies.get("username")
            cookie_password = request.cookies.get("password")

            if (cookie_username == current_username) and (cookie_password == current_password):

                # Redirect to homepage
                return make_response(render_template("index.html"), cookie_username), 302
            else:

                # Set a flashed massage
                flash("Error: Your credentials are not correct or you need to register")

                # reload with showing flash massage
                return make_response(render_template("login.html")), 302
        else:

            # Set a flashed massage
            flash("Error: One field is empty or both")

            # reload with showing flash massage
            return make_response(render_template("login.html")), 302


    return render_template("login.html")

# Register page logic
@app.route("/register", methods=["GET", "POST"])
def register():

    # If cookies are None in GET request
    if request.cookies.get("username") == None or request.cookies.get("password") == None:
        
        # Make a response, initialize cookies and reload the page
        return init_cookines("register.html", 5), 302

    
    if request.method == "POST":

        # Modify response
        response = make_response(render_template("register.html"))

        # Get form data from in register page
        new_user = request.form.get("new_username").strip()
        new_password = request.form.get("new_password")

        # Validate data emptiness
        if len(new_user) > 0 and len(new_password) > 0:

            # Update the cookies with the new credentials
            response.set_cookie("username", new_user, max_age= 5 * DAY)
            response.set_cookie("password", new_password, max_age= 5 * DAY)

            # Set the redirect url
            response.headers["Location"] = url_for("register")

            flash("You registered successfully, you will redirect to homepage after", "success")
            
            return response, 302
        else:

            # Set a flashed massage
            flash("Error: Empty fields are not allowed", 'error')

            # Applay cookies changes and redirect to login page
            return redirect(url_for("register"))

    # Make a response and reload the page
    return make_response(render_template("register.html")), 302

# Logout page logic
@app.route("/logout")
def logout():

    # Cookies data
    cookie_username = request.cookies.get("username")
    cookie_password = request.cookies.get("password")

    # If cookies are None in GET request
    if cookie_username == None or cookie_password == None:
        
        # Make a response, initialize cookies and redirect to log in page
        return init_cookines("login.html", 5), 302

    # If cookies are exist, then make them empty, and redirect to log in page
    
    if cookie_username and cookie_password:

        # Modify response
        response = make_response(render_template("logout.html"))

        # Remove cookies
        response.set_cookie("username", "", max_age= 0)
        response.set_cookie("password", "", max_age= 0)

        return response

    return render_template("logout.html")

