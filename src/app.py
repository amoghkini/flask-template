from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Temporary user data (replace this with a database later)
users = {
    'user1': {'password': 'pass123'},
    'user2': {'password': 'pass456'}
}


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
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = {'password': password}
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('signup.html', error='Username already taken.')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_valid_credentials(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
