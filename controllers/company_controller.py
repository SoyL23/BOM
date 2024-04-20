from db.db import db
from model.company_model import Company

class Company_Controller():

    def __init__(self):
        pass

    def create_company(self, company_data:dict):
        try:
            company:object = Company(**company_data)
            with db.session.begin():
                db.session.add(company)
                db.session.commit()
            return 'Company created successfully.'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    def read_company(self, id:int):
        try:
            company = db.session.query(Company).filter(Company.id  == id).first()
            if company:
                return company.to_dict()
            else:
                return 'Company not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()
        

    def read_companies(self):
        try:
            companies = db.session.query(Company).all()
            if companies:
                data:dict = {company.id: company.to_dict() for company in companies}
                return data
            else:
                return 'Companies not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()



    def update_company(self, id:int, new_data:dict):
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
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()


    def delete_company(self, id:int):
        try:
            company = db.session.query(Company).filter(Company.id  == id).first()
            if company:
                db.session.delete(company)
                db.session.commit()
                return 'Company deleted successfully'
            else:
                return 'Company not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()