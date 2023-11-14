import os
from flask import send_from_directory
from flask.views import MethodView
from config.config import STATIC_FOLDER


class ProfilePicAPI(MethodView):

    def get(self):
        return send_from_directory(os.path.join(STATIC_FOLDER, 'images'), 'default_profile_pic.jpg')
