from db.db import *
from model.country_model import *
from model.state_model import *
from model.city_model import *
from model.role_model import *
from model.user_model import *
from model.user_data_model import *
from model.user_model import *
from model.course_model import *
from model.evaluation_model import *
from model.certificate_model import *
from model.client_model import *
from model.company_model import *
from model.employee_model import *
from model.sell_model import *
from model.shopping_model import *
# from model.sell_course_model import *

class Main():

   def __init__(self): 
   
      if __name__ == '__main__':

         Base.metadata.create_all(db.engine)

main = Main()