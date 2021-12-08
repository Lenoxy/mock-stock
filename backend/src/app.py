from flask_login import LoginManager
from flasgger import Swagger
from flask_cors import CORS
from flask import Flask
import db


def create_app():
    app = Flask(__name__)
    CORS(app=app, supports_credentials=True)

    swagger = Swagger(app)
    swagger.load_swagger_file('openapi.yaml')

    add_flask_login(app)

    # Add Endpoints / Resources from Controller to app
    from controller.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from controller.me import me as me_blueprint
    app.register_blueprint(me_blueprint)

    from controller.stocks import stocks as stocks_blueprint
    app.register_blueprint(stocks_blueprint)

    from controller.users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    # Endpoint for swagger dok
    from controller.swagger import swagger as swagger_blueprint
    app.register_blueprint(swagger_blueprint)

    return app


def add_flask_login(app):
    app.secret_key = 'super secret string'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(username):
        return db.get_user(username)

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return 'Unauthorized', 401


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)
