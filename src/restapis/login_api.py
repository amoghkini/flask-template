from flask import render_template, g, redirect, url_for, request, session
from flask.views import MethodView


class LogInAPI(MethodView):

    def get(self):
        if g.user:
            return redirect(url_for('dashboard_api'))
        return render_template('login.html')

    def post(self):
        username = request.form['email']
        password = request.form['password']
        
        
        if is_valid_credentials(username, password):
            session['user'] = username
            # Get notifications for this user (replace with your logic)
            # user_notifications = notifications
            # session['notifications'] = user_notifications
            return redirect(url_for('index_api'))
        else:
            return render_template('login.html', error='Invalid username or password.')
        
def is_valid_credentials(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

users = {
    'user1': {'password': 'pass123'},
    'user2': {'password': 'pass456'}
}