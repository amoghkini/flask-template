from flask import render_template, g, redirect, url_for
from flask.views import MethodView


class ProfileAPI(MethodView):

    def get(self):
        if not g.user:
            return redirect(url_for('index_api'))
        profile_data = {"first name": "Amogh",
                    "last name": "Kini",
                    "email": "amogh@mail.com",
                    "date of birth": "10 Jan 2022",
                    "last_login": "10 Aug 2023 02:30",
                    "password": "asasd"}
        return render_template('profile.html', profile_data = profile_data)
