from typing import Dict
from flask import render_template, g, redirect, url_for, request, session, flash
from flask.views import MethodView

from config.config import get_server_config
from exceptions.user_exceptions import AuthUserError
from user.user_methods import UserMethods
from user.user_status import UserStatus


class LogInAPI(MethodView):

    def get(self):
        if g.user:
            return redirect(url_for('dashboard_api'))
        return render_template('login.html')
      
    def post(self):
        try:
            session.pop('user', None)
            
            email_id: str = request.form.get("email")
            password: str = request.form.get("password")
            
            user: Dict = {"email_id": email_id,
                          "password": password}
            
            user_data: Dict = UserMethods.login_user(user)
            
            acct_activation_req = get_server_config().get('accountActivationRequired')
            if (user_data.get('account_status') == UserStatus.CREATED) and acct_activation_req:
                # Activate account
                UserMethods.activate_account(email_id)
                flash('Account activation link sent on registered email address. Please activate account before login!!!', 'success')
                return redirect(url_for('login_api'))
            
            session['user'] = user_data.get('username')
            flash('Logged In Successfully!!!', 'success')
            return redirect(url_for('index_api'))
        
        except AuthUserError as e:
            flash(str(e), 'danger')
            return render_template('login.html')
        except Exception as e:
            flash(str(e), 'danger')
            return render_template('login.html')
        
        
        # if is_valid_credentials(username, password):
        #     session['user'] = username
        #     # Get notifications for this user (replace with your logic)
        #     # user_notifications = notifications
        #     # session['notifications'] = user_notifications
        #     return redirect(url_for('index_api'))
        # else:
        #     return render_template('login.html', error='Invalid username or password.')
        
def is_valid_credentials(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

users = {
    'user1': {'password': 'pass123'},
    'user2': {'password': 'pass456'}
}