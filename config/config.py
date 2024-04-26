import os
from dotenv import load_dotenv
class Config:

    #Esta clase crea el String que se usa como motor de consultas SQL
    
    def __init__(self):

        load_dotenv()
        # self.__data:dict = self.__load_config()
        self.__user:str = os.getenv('DB_USER')
        self.__password:str = os.getenv('DB_PASSWORD')  
        self.__host:str = os.getenv('DB_HOST')
        self.__db:str = os.getenv('DB_NAME')

    @property
    def engine(self) -> str:
        return f'mysql://{self.__user}:{self.__password}@{self.__host}/{self.__db}'
    
    def __load_config(self) -> dict:
        data_config:dict = {}
        with open('.env', 'r') as env_data:
            for line in env_data:
                name, data = line.strip().split('=')
                data_config[name]=data
        return data_config

class ConfigDev:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'{Config.engine}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')