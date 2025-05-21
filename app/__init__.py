from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')  

    db = SQLAlchemy(app)
    login_manager = LoginManager()

    db.init_app(app)
    login_manager.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # or your DB URIflask db migrate -m "Initial migration"
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()


    from .routes.blog_routes import blog
    from .routes.auth_routes import auth
    app.register_blueprint(blog)
    app.register_blueprint(auth)

    return app






