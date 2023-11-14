from flask import render_template, g, redirect, url_for
from flask.views import MethodView

class IndexAPI(MethodView):
    def get(self):
        if g.user:
            return render_template('dashboard.html', username=g.user)
        return render_template('index.html')