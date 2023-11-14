import os
from typing import Tuple
from common.execution_env import ExecutionEnv
from config.config import get_server_config, BaseConfig, DevConfig, TestingConfig, StagingConfig, ProdConfig


class Utils:
    
    @staticmethod
    def get_config() -> BaseConfig:
        """
        Retrieve the appropriate configuration object based on the current execution environment.

        Returns:
            BaseConfig: An instance of the configuration class (DevConfig, TestingConfig,
            StagingConfig, or ProdConfig) corresponding to the current execution environment.

        Raises:
            ValueError: If the current execution environment is not one of the predefined
            values (DEV, TEST, STAGE, or PROD).

        Example:
            To obtain the configuration for the current execution environment:
            
            >>> config = Utils.get_config()
            >>> print(config.DEBUG)
        """
        env = Utils.get_execution_env()
        if env == ExecutionEnv.DEV:
            config = DevConfig()
        elif env == ExecutionEnv.TEST:
            config = TestingConfig()
        elif env == ExecutionEnv.STAGE:
            config = StagingConfig()
        elif env == ExecutionEnv.PROD:
            config = ProdConfig()
        else:
            raise ValueError("Invalid environment provided")
        return config

    @staticmethod
    def get_execution_env() -> str:
        """
        Retrieve the environment setting from the server configuration.

        This function reads the server configuration data, typically loaded from a 'server.json' file,
        and returns the value associated with the 'env' key. The 'env' key is expected to specify
        the current execution environment, such as 'development', 'testing', 'staging' or 'production'.

        Returns:
            environment: The environment setting as a string.

        Example:
            To obtain the current execution environment setting from the server configuration:

            >>> environment = get_execution_env()
            >>> print(f"Current environment: {environment}")
        """
        env = get_server_config().get('env')
        return env
    
    @staticmethod
    def get_log_dir():
        return get_server_config().get('logFileDir')
    
    @staticmethod
    def validate_execution_env() -> None:
        env: str = Utils.get_execution_env()
        
        valid_executions: Tuple = (ExecutionEnv.DEV, ExecutionEnv.TEST, ExecutionEnv.PROD)
        if env not in valid_executions:
            print("The execution environment ", env, "is not valid!!!.")
            print("The valid executions are ", valid_executions)
            exit(1)
            
    @staticmethod
    def set_environment_variables() -> None:
        os.environ["DB_HOST"] = get_server_config().get('DB_HOST')
        os.environ["DB_PORT"] = get_server_config().get('DB_PORT')
        os.environ["DB_USER"] = get_server_config().get('DB_USER')
        os.environ["DB_PASSWORD"] = get_server_config().get('DB_PASSWORD')
        os.environ["DB_SCHEMA"] = get_server_config().get('DB_SCHEMA')