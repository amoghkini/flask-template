from app.app import create_app
from config.config import get_server_config
from flask import render_template
app = create_app()

server_config = get_server_config()
port = server_config.get('port')

@app.route('/data_table')
def data_table():
    # Replace this with your data retrieval logic (list of dictionaries)
    data = [
        {'column1': 'Value 1', 'column2': 'Value 2'},
        {'column1': 'Value 3', 'column2': 'Value 4'},
        # Add more data rows as needed
    ]
    # data = []
    return render_template('data_table.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=port)
