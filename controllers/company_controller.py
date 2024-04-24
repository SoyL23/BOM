from db.db import db
from models.company_model import Company
from sqlalchemy.exc import SQLAlchemyError

class Company_Controller():

    def __init__(self):
        pass

#---INIT CREATE COMPANY CONTROLLER---#
    def create_company(self, company_data:dict) -> str:
        try:
            company:object = Company(**company_data)
            with db.session.begin():
                db.session.add(company)
                db.session.commit()
            return 'Company created successfully.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END CREATE COMPANY CONTROLLER---#

#---INIT READ COMPANY CONTROLLER---#
    def read_company(self, id:int) -> str | dict:
        try:
            company = db.session.query(Company).filter(Company.id  == id).first()
            if company:
                return company.to_dict()
            else:
                return 'Company not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END READ COMPANY CONTROLLER---#
        

#---INIT READ ALL COMPANIES CONTROLLER---#
    def read_companies(self) -> str | dict:
        try:
            companies = db.session.query(Company).all()
            if companies:
                data:dict = {company.id: company.to_dict() for company in companies}
                return data
            else:
                return 'Companies not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END READ ALL COMPANIES CONTROLLER---#


#---INIT UPDATE COMPANY CONTROLLER---#
    def update_company(self, id:int, new_data:dict) -> str:
        try:
            company = db.session.query(Company).filter(Company.id  == id).first()
            if company:
                for attribute, data in new_data.items():
                    if attribute != 'id':
                        setattr(company, attribute, data)
                db.session.commit()
                return 'Company updated successfully.'             
            else:
                return 'Company not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END UPDATE COMPANY CONTROLLER---#

#---INIT DELETE COMPANY CONTROLLER---#
    def delete_company(self, id:int) -> str:
        try:
            company = db.session.query(Company).filter(Company.id  == id).first()
            if company:
                db.session.delete(company)
                db.session.commit()
                return 'Company deleted successfully'
            else:
                return 'Company not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
#---END DELETE COMPANY CONTROLLER---#