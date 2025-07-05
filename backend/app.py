from flask import Flask
from flask_security import Security

from flask_restful import Api

from flask_cors import CORS

from controllers.database import db
from controllers.config import Config
from controllers.user_datastore import user_datastore

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    security = Security(app, user_datastore)

    api = Api(app, prefix='/api')

    with app.app_context():
        db.create_all()

        admin_role = user_datastore.find_or_create_role(name='admin', description='Administrator')
        user_role = user_datastore.find_or_create_role(name='user', description='Regular User')

        if not user_datastore.find_user(email='admin@gmail.com'):
            user_datastore.create_user(
                email = "admin@gmail.com",
                password = "admin123",
                roles=[admin_role]
            )
        
        db.session.commit()

    return app, api


app, api = create_app()
CORS(app, origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ])
# @app.route('/')
# def index():
#     return {
#         'message': 'Welcome to the Flask Security API!'
#     }, 200

# @app.route('/something/<int:id>', methods=['POST'])
# def something(id):
#     pass

# @app.route('/something', methods=['PUT'])
# def something_put():
#     pass

# class Index(Resource):
#     def get(self):
#         return {
#             'message': 'Welcome to the Flask Security API!'
#         }, 200  
    
# api.add_resource(Index, '/')

from controllers.authentication_apis import LoginAPI, LogoutAPI, RegisterAPI
api.add_resource(LoginAPI, '/login')
api.add_resource(LogoutAPI, '/logout')
api.add_resource(RegisterAPI, '/register')

from controllers.crud_apis import CategoryCrudAPI
api.add_resource(CategoryCrudAPI, '/categories', '/categories/<int:category_id>')

if __name__ == "__main__":
    app.run(debug=True)