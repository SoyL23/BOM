from models.certificate_model import Certificate
from db.db import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError
from typing import List

class Certificate_Controller:
    
    def create_certificate(self, certificate: Certificate) -> str:
        try:
            with db.session.begin():
                db.session.add(certificate)
                db.session.commit()
                return 'Certificate created successfully.'   
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_certificate(self, id: int) -> str|dict:
        try:
            with db.session.begin():
                certificate:Certificate = db.session.query(Certificate).get(ident=id)
                if certificate:
                    return certificate.to_dict()
                else:
                    return 'Certificate not found.'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_certificates(self) -> str|dict:
        try:
            with db.session.begin():
                certificates:List[Certificate] = db.session.query(Certificate).all()
                if certificates:
                    data = {certificate.id: certificate.to_dict() for certificate in certificates}
                    return data
                else:
                    return 'Certificates not found'  
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'        
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
    
    def update_certificate(self, id: int, new_data: dict) -> str:
        try:
            with db.session.begin():
                certificate:Certificate = db.session.query(Certificate).get(ident=id)
                if certificate:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(certificate, attribute, data)
                    db.session.commit()
                    return 'Certificate updated successfully'
                else: 
                    return 'Certificate not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'        
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def delete_certificate(self, id: int) -> str:
        try:
            with db.session.begin():
                certificate:Certificate = db.session.query(Certificate).get(ident=id)
                if certificate:
                    db.session.delete(certificate)
                    db.session.commit()
                    return 'Certificate deleted successfully'
                else:
                    return 'Certificate not found'
        except SQLAlchemyError as e:
            db.session.rollback()
            return f'DATABASE ERROR: {str(e)}'        
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()