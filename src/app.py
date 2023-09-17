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
            # user_notifications = notifications
            # session['notifications'] = user_notifications
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
    'TestDropdown': ["Value 1", "Value 2", "Value 3"],
    'Gender': ["Male", "Female"],
}


@app.route('/get_dropdown_data/<page>', methods=['GET'])
def get_dropdown_data(page):
    # Fetch the values for the specified page
    data = dropdown_values.get(page, [])
    return jsonify(data)

# class Notification:
#     def __init__(self, message, is_read=False):
#         self.message = message
#         self.is_read = is_read
        

# notifications = []  # Initialize an empty list to store notifications


class Notification:
    def __init__(self, id, title, message, timestamp, read):
        self.id = id
        self.title = title
        self.message = message
        self.timestamp = timestamp
        self.is_read = read


# Sample hardcoded notification data as a list of Notification objects
notifications = [
    Notification(1, 'New Message', 'You have received a new message from John Doe.',
                 '2023-09-16 10:30:00', False),
    Notification(2, 'Friend Request', 'You have a new friend request from Jane Smith.',
                 '2023-09-15 14:45:00', True),
    Notification(3, 'Event Reminder', 'Don\'t forget about the team meeting today at 3:00 PM.',
                 '2023-09-14 16:00:00', False),
    Notification(4, 'Payment Received',
                 'Your payment of $100 has been received successfully.', '2023-09-13 09:15:00', True),
    Notification(5, 'New Article Published',
                 'Check out our latest article on web development trends.', '2023-09-12 11:30:00', False)
]


@app.route('/add_notification/<message>')
def add_notification(message):
    notification = Notification(message)
    notifications.append(notification)
    return jsonify({"message": "Notification added successfully"})


@app.route('/get_notifications')
def get_notifications():
    unread_notifications = [n.__dict__ for n in notifications if not n.is_read]
    return jsonify({"notifications": unread_notifications})


@app.route('/mark_notifications_as_read')
def mark_notifications_as_read():
    for notification in notifications:
        notification.is_read = True
    return jsonify({"message": "All notifications marked as read"})



# Simulate a variable to store the dark mode status
dark_mode_status = False


@app.route('/api/get-dark-mode', methods=['GET'])
def get_dark_mode():
    global dark_mode_status
    print("Dark mode statys", dark_mode_status)
    return jsonify({'darkMode': dark_mode_status})


@app.route('/api/set-dark-mode', methods=['POST'])
def set_dark_mode():
    global dark_mode_status
    data = request.get_json()
    if 'darkMode' in data:
        dark_mode_status = data['darkMode']
        return jsonify({'message': 'Dark mode status updated successfully'})
    else:
        return jsonify({'error': 'Dark mode status not provided in the request'})

if __name__ == '__main__':
    app.run(debug=True)
