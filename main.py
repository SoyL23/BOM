from db.db import *
from models.country_model import *
from models.state_model import *
from models.city_model import *
from models.role_model import *
from models.user_model import *
from models.user_data_model import *
from models.user_model import *
from models.course_model import *
from models.evaluation_model import *
from models.certificate_model import *
from models.client_model import *
from models.company_model import *
from models.employee_model import *
from models.sell_model import *
from models.shopping_model import *
# from model.sell_course_model import *

class Main():

   def __init__(self): 
   
      if __name__ == '__main__':
         self.create_tables()
         
   def create_tables(self):
      Base.metadata.create_all(db.engine)

main = Main()
