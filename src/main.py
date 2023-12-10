from app.app import create_app
from config.config import get_server_config

app = create_app()

server_config = get_server_config()
port = server_config.get('port')

from flask import request, jsonify
# Route to get section data in JSON format
@app.route('/get_section_data', methods=['GET'])
def get_section_data():
    section = request.args.get('section')
    if section == 'section1':
        # Fetch data for Section 1 (replace with your logic)
        section_data = [
            {"ID": 1, "Name": "Item 1"},
            {"ID": 2, "Name": "Item 2"},
            # Add more data as needed
        ]
    elif section == 'section2':
        # Fetch data for Section 2 (replace with your logic)
        section_data = [
            {"ID": 3, "Name": "Item 3"},
            {"ID": 4, "Name": "Item 4"},
            # Add more data as needed
        ]
    elif section == 'section3':
        # Fetch data for Section 3 (replace with your logic)
        section_data = [
            {"ID": 5, "Name": "Item 5"},
            {"ID": 6, "Name": "Item 6"},
            # Add more data as needed
        ]
    else:
        section_data = []  # Empty data if section is invalid

    return jsonify(section_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=port)
