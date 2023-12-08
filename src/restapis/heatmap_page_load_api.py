from flask import render_template
from flask.views import MethodView


class HeatmapPageLoadAPI(MethodView):

    def get(self):
        return render_template('heatmap.html')
