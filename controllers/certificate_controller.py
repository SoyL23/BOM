from models.certificate_model import Certificate
from db.db import db

class Controller:
    
    def create_certificate(self, certificate:object)-> str:
        try:
            with db.session.begin():
                db.session.add(certificate)
                db.session.commit()
                return 'Certificate created successfully.'   
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def read_certificate(self, id:int) -> str|dict:
        try:
            with db.session.begin():
                 certificate = db.session.query(Certificate).filter(Certificate.id == id).first()
                 if certificate:
                     return certificate.to_dict()
                 else:
                     return 'Certificate not found.'
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def read_all(self) -> str|dict:
        try:
            with db.session.begin():
                certificates = db.session.query(Certificate).all()
                if certificates:
                    data = {certificate.id:certificate.to_dict() for certificate in certificates}
                    return data
                else:
                    return 'Certificates not found'  
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update_certificate(self, id:int, new_data:dict) -> str:
        try:
            with db.session.begin():
                certificate = db.session.query(Certificate).filter(Certificate.id == id).first()
                if certificate:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(certificate, attribute, data)
                    db.session.commit()
                    return 'Certificate updatep successfully'
                else: 
                    return 'Certificate not found'
        except Exception as e:
            db.session.rollback()
            return str(e)
        finally:
            db.session.close()

    # def delete_certificate(self):
    #     try:
    #         with db.session.begin():
    #             db.session.delete()
    #             db.session.commit()
    #     except:
    #         db.session.rollback()
    #     finally:
    #         db.session.close()