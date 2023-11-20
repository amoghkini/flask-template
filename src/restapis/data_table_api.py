from flask import render_template
from flask.views import MethodView


class DataTableAPI(MethodView):

    def get(self):
        data = [
        {'column1': 'Value 1', 'column2': 'Value 2'},
        {'column1': 'Value 3', 'column2': 'Value 4'},
        # Add more data rows as needed
    ]
        return render_template('data_table.html', data=data)
