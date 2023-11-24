from app.app import create_app
from config.config import get_server_config
from flask import session, jsonify, request
app = create_app()

server_config = get_server_config()
port = server_config.get('port')

# @app.route('/api/user/role', methods=['GET'])
# def get_user_role():
#     print("Amogh is here")
#     if True:
#         print("Inside if condition")
#         return jsonify({'role': "admin"})

#     return jsonify({'error': 'Role not found'})

# # Endpoint to update user role
# @app.route('/api/user/role', methods=['PUT'])
# def update_user_role():
#     data = request.get_json()
#     if 'role' in data:
#         print("The new role is ", data['role'])
#         return jsonify({'message': 'User role updated successfully'})
#     return jsonify({'error': 'Role not provided'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=port)
