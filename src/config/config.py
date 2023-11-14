import json
import os
from datetime import timedelta


APP_NAME: str = "Flask boilerplate"
PROJECT_ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TEMPLATE_FOLDER: str = os.path.join(PROJECT_ROOT, 'templates')
STATIC_FOLDER: str = os.path.join(PROJECT_ROOT, 'static')


def get_server_config():
    """
    Load and return the server configuration data from a JSON file.

    This function reads the 'server.json' file from the relative path '../config/',
    parses its contents as JSON, and returns the resulting JSON data, which typically
    contains server configuration parameters.

    Returns:
        dict: A dictionary containing server configuration data.

    Example:
        To retrieve server configuration data from the 'server.json' file:

        >>> server_config = get_server_config()
        >>> print(server_config.get('env'))
    """
    with open('../config/server.json', 'r') as server:
        json_server_data = json.load(server)
        return json_server_data


class BaseConfig(object):
    
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY','This is secret key')
    
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=get_server_config().get('sessionLifetime'))


class DevConfig(BaseConfig):
    ENV =  'dev'
    DEBUG = True 
    
    
class TestingConfig(BaseConfig):
    ENV = 'qa'
    DEBUG = False
    TESTING = True


class StagingConfig(BaseConfig):
    ENV = 'stage'
    DEBUG = False


class ProdConfig(BaseConfig):

    ENV = 'prod'
    DEBUG = False