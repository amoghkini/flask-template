from flask import render_template, g, redirect, url_for
from flask.views import MethodView

class DashboardAPI(MethodView):
    def get(self):
        if not g.user:
            return redirect(url_for('index_api'))
        return render_template('dashboard.html', username=g.user)