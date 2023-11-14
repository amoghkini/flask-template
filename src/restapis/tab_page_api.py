from flask import render_template
from flask.views import MethodView


class TabPageAPI(MethodView):

    def get(self):
        return render_template('sample_page_with_tab.html')
