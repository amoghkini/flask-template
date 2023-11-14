from flask import render_template
from flask.views import MethodView


class ContactUsAPI(MethodView):

    def get(self):
        return render_template('contact_us.html')
