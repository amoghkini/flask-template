from flask import render_template
from flask.views import MethodView


class ChangePasswordAPI(MethodView):

    def get(self):
        return render_template('change_password.html')
