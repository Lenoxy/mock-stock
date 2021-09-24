from flask import Flask

# init SQLAlchemy so we can use it later in our models
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Add Endpoints / Resources from Controller to app
    from controller.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from controller.me import me as me_blueprint
    app.register_blueprint(me_blueprint)

    from controller.stocks import stocks as stocks_blueprint
    app.register_blueprint(stocks_blueprint)

    from controller.users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)
