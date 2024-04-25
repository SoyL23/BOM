from app import app
from main import Main
from db.db import db

class Index():

    def __init__(self):

        with app.app_context():

            main = Main()

    def run(self):
        return app.app.run()
            
index = Index()

index.run()