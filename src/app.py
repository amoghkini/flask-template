from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Temporary user data (replace this with a database later)
users = {
    'user1': {'password': 'pass123'},
    'user2': {'password': 'pass456'}
}

notifications = [
    {"id": 1, "message": "Notification 1"},
    {"id": 2, "message": "Notification 2"},
    # Add more notifications here
]

def is_valid_credentials(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact_us.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the form data from the request
        first_name = request.form.get('firstName')
        # Perform backend validation
        errors = {}
        if len(first_name) < 5:
            errors['firstName'] = f'First name should be at least 5 characters long \n Please provide the valid data'

            # Assuming there's an error with confirmPassword validation
            # errors['confirmPassword'] = "Password and confirm password should be same"

        # If there are errors, render the template with error messages
        if errors:
            return render_template('signup.html', form_data=request.form, errors=errors)

        # If no errors, proceed with form submission logic
        # ... (your form submission logic here)
        print("Going to login page")
        return redirect(url_for('login'))  # Redirect to a success page

    return render_template('signup.html', form_data=request.form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        if is_valid_credentials(username, password):
            session['user'] = username
            # Get notifications for this user (replace with your logic)
            user_notifications = notifications
            session['notifications'] = user_notifications
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

@app.route('/profile_picture', methods=['GET'])
def profile_picture():
    return send_from_directory('static', 'images/default_profile_pic.jpg')

@app.route('/profile')
def profile():
    profile_data = {"first name": "Amogh",
                    "last name": "Kini",
                    "email": "amogh@gmail.com",
                    "date of birth": "10 Jan 2022",
                    "last_login": "10 Aug 2023 02:30",
                    "password": "asasd"}
    return render_template('profile.html', profile_data = profile_data)

@app.route('/tab_page')
def tab_page():
    return render_template('sample_page_with_tab.html')

@app.route('/change_password', methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        print("Change password")
    return render_template('change_password.html')

@app.route('/account')
def account():
    profile_data = {"first_name": "Amogh",
                    "last name": "Kini",
                    "email": "amogh@gmail.com",
                    "date of birth": "10 Jan 2022",
                    "last_login": "10 Aug 2023 02:30",
                    "password": "asasd"}
    
    return render_template('account.html', form_data=profile_data)


dropdown_values = {
    'page1': ["Value 1", "Value 2", "Value 3"],
    'Gender': ["Male", "Female"],
}


@app.route('/get_dropdown_data/<page>', methods=['GET'])
def get_dropdown_data(page):
    # Fetch the values for the specified page
    data = dropdown_values.get(page, [])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
