from flask import jsonify, redirect, url_for, session
from flask.views import MethodView

class LogOutAPI(MethodView):

    def get(self):
        session.pop('user',None)
        redirect_url = url_for('login_api')  # Get the URL for login_api
        return jsonify({'message': 'Logged out successfully', 'redirect_url': redirect_url})

