from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import utils, auth_token_required , roles_required

from controllers.database import db
from controllers.models import *

#CRUD APIs for the Categories

class CategoryCrudAPI(Resource):
    def get(self, category_id = None):
        if category_id:
            category = Categories.query.get(category_id)
            if not category:
                return make_response(jsonify({'message': 'Category not found.'}), 404)

            response = {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }

            return make_response(jsonify(response), 200)
        
        else:
            categories = Categories.query.all()
            response = []
            for category in categories:
                response.append({
                    'id': category.id,
                    'name': category.name,
                    'description': category.description
                })
            return make_response(jsonify(response), 200)
        
    @auth_token_required
    @roles_required('admin')    
    def post(self):
        data = request.get_json()

        if not data:
            return make_response(jsonify({'message': 'No input data provided.'}), 400)
        
        name = data.get('name')
        description = data.get('description')

        if not name:
            return make_response(jsonify({'message': 'Category name is required.'}), 400)
        
        new_category = Categories(name=name, description=description)
        db.session.add(new_category)
        db.session.commit()

        response = {
            'message': 'Category created successfully.',
            'data': {
                'id': new_category.id,
                'name': new_category.name,
                'description': new_category.description
            }
        }
        return make_response(jsonify(response), 201)
    
    @auth_token_required
    @roles_required('admin')
    def put(self, category_id):

        category = Categories.query.get(category_id)

        if not category:
            return make_response(jsonify({'message': 'Category not found.'}), 404)
        
        data = request.get_json()

        if not data:
            return make_response(jsonify({'message': 'No input data provided.'}), 400)
        
        name = data.get('name')
        description = data.get('description')

        if name:
            existing_category = Categories.query.filter_by(name=name).first()
            if existing_category and existing_category.id != category_id:
                return make_response(jsonify({'message': 'Category name already exists.'}), 400)
            
            category.name = name

        if description:
            category.description = description

        db.session.commit()

        response = {
            'message': 'Category updated successfully.',
            'data': {
                'id': category.id,
                'name': category.name,
                'description': category.description
            }
        }
        return make_response(jsonify(response), 200)
    
    @auth_token_required
    @roles_required('admin')
    def delete(self, category_id):
        category = Categories.query.get(category_id)

        if not category:
            return make_response(jsonify({'message': 'Category not found.'}), 404)
        
        db.session.delete(category)
        db.session.commit()

        response = {
            'message': 'Category deleted successfully.'
        }
        return make_response(jsonify(response), 200)