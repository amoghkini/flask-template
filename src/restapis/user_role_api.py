from flask import jsonify, request, g
from flask.views import MethodView

from user.user_methods import UserMethods

class UserRoleAPI(MethodView):

    def get(self):
        user_role = UserMethods.get_user_role(g.user)
        return jsonify({'role': user_role})
    
    def put(self):
        data = request.get_json()
        if 'role' in data:
            print("The new role is ", data['role'])
            return jsonify({'message': 'User role updated successfully'})
        return jsonify({'error': 'Role not provided'})