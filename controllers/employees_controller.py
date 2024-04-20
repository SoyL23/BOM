from model.employee_model import Employee
from db.db import db

class Employee_Controller:
    
    def create_employee(self, employee_data:dict) -> str:
        try:
            employee = Employee(**employee_data)
            with db.session.begin():
                db.session.add(employee)
                db.session.commit()
                return 'Employee created successfully.'    
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()
    
    def read_employee(self, id:int)-> str | dict:
        try:
            with db.session.begin():
                employee = db.session.query(Employee).filter(Employee.id == id).first()
                if employee:
                    return employee.to_dict()
                else:
                    return 'Employee not found'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def read_employees(self) -> str | dict:
        try:
            with db.session.begin():
                employees = db.session.query(Employee).all()
                if employees:
                    data = {employee.id:employee.to_dict() for employee in employees}
                    return data
                else:
                    return 'Not Empoyees Found'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def update_employee(self, new_data:dict) -> str:
        try:
            with db.session.begin():
                employee = db.session.query(Employee).filter(Employee.id == id).first()
                if employee:
                    for attribute, data in new_data.items():
                        if attribute != 'id':
                            setattr(employee, attribute, data)
                    return 'Employee updated successfully.'
                else:
                    return 'Employee Not Found'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()

    def delete_employee(self) -> str:
        try:
            employee = db.session.query(Employee).filter(Employee.id == id).first()
            if employee:
                with db.session.begin():
                    db.session.delete(employee)
                    db.session.commit()
                    return 'Employee deleted successfully.'
            else:
                return 'Employee Not Found'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
        finally:
            db.session.close()