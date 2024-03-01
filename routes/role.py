from flask import Blueprint, jsonify, request
from config.db import db
from model.role import Role
from services.generate_token import generate_token                                   

role = Blueprint('role', __name__)

@role.route('/api/role/get/list', methods=['GET'])
def get_roles():
    
    roles = Role.query.all()
    return jsonify([role.to_dict() for role in roles])

@role.route('/api/role/get/<int:id>', methods=['GET'])
def get_role(id):
    role = Role.query.get(id)
    if role:
        return jsonify(role.to_dict())
    else:
        return jsonify({'message': 'Role not found'}), 404

@role.route('/api/role/create', methods=['GET','POST'])
def create_role():
    if request.method == 'GET':
        token = generate_token()
        return token
    else:
        with db.session.begin():
            data = request.get_json()
            role_name = data.get('role_name')
            role_description = data.get('role_description')
            
            new_role = Role(role_name=role_name, role_description=role_description)
            db.session.add(new_role)
            db.session.commit()
            db.session.close()

        return jsonify({'message': 'Role created successfully'}), 201

@role.route('/api/role/edit/<int:id>', methods=['POST'])
def update_role(id):
    role = Role.query.get(id)
    if role:
        data = request.get_json()
        role.role_name = data.get('role_name', role.role_name)
        role.role_description = data.get('role_description', role.role_description)
        db.session.commit()
        db.session.close()
        return jsonify({'message': 'Role updated successfully'})
    else:
        return jsonify({'message': 'Role not found'}), 404

@role.route('/api/role/delete/<int:id>', methods=['POST'])
def delete_role(id):
    role = Role.query.get(id)
    if role:
        db.session.delete(role)
        db.session.commit()
        db.session.close()
        db.session.close()
        return jsonify({'message': 'Role deleted successfully'})
    else:
        return jsonify({'message': 'Role not found'}), 404
