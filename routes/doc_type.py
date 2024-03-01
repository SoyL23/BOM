from flask import Blueprint, jsonify, request
from config.db import db
from model.doc_type import Doc_Type
from services.generate_token import generate_token

doc_type = Blueprint('doc_type', __name__)

@doc_type.route('/api/doc_type/get/list', methods=['GET'])
def get_doc_types():
    doc_types = Doc_Type.query.all()
    return jsonify([doc_type.to_dict() for doc_type in doc_types])

@doc_type.route('/api/doc_type/get/<int:id>', methods=['GET'])
def get_doc_type(id):
    doc_type = Doc_Type.query.get(id)
    if doc_type:
        return jsonify(doc_type.to_dict())
    else:
        return jsonify({'message': 'Doc Type not found'}), 404

@doc_type.route('/api/doc_type/create', methods=['GET', 'POST'])
def create_doc_type():
    if request.method == 'GET':
        token = generate_token()
        return token
    else:
        with db.session.begin():
            data = request.get_json()
            type_doc_name = data.get('type_doc_name')
            type_doc_description = data.get('type_doc_description')
            
            new_doc_type = Doc_Type(type_doc_name=type_doc_name, type_doc_description=type_doc_description)
            db.session.add(new_doc_type)
            db.session.commit()
        return jsonify({'message': 'Doc Type created successfully'}), 201

@doc_type.route('/api/doc_type/edit/<int:id>', methods=['POST'])
def update_doc_type(id):
    doc_type = Doc_Type.query.get(id)
    if doc_type:
        data = request.get_json()
        doc_type.type_doc_name = data.get('type_doc_name', doc_type.type_doc_name)
        doc_type.type_doc_description = data.get('type_doc_description', doc_type.type_doc_description)
        db.session.commit()
        return jsonify({'message': 'Doc Type updated successfully'})
    else:
        return jsonify({'message': 'Doc Type not found'}), 404

@doc_type.route('/api/doc_type/delete/<int:id>', methods=['POST'])
def delete_doc_type(id):
    doc_type = Doc_Type.query.get(id)
    if doc_type:
        db.session.delete(doc_type)
        db.session.commit()
        return jsonify({'message': 'Doc Type deleted successfully'})
    else:
        return jsonify({'message': 'Doc Type not found'}), 404
