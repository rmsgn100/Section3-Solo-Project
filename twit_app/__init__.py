import os
from flask import Flask
from twit_app.routes import main_routes, add_routes, get_routes, delete_routes, update_routes, compare_routes
from twit_app.models import db, migrate
from dotenv import load_dotenv
load_dotenv()

# DATABASE_URI = "sqlite:///twit.sqlite3"
DATABASE_URI = os.getenv('DATABASE_URL')

# factory pattern
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_routes.main_routes)
    app.register_blueprint(add_routes.add_routes, url_prefix='/add')
    app.register_blueprint(get_routes.get_routes, url_prefix='/get')
    app.register_blueprint(delete_routes.delete_routes, url_prefix='/delete')
    app.register_blueprint(update_routes.update_routes, url_prefix='/update')
    app.register_blueprint(compare_routes.compare_routes, url_prefix='/compare')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
