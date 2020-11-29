from flask import Flask
from twit_app.routes import main_routes, add_routes, get_routes, delete_routes, update_routes, compare_routes
from twit_app.models import db, migrate


DATABASE_URI = "sqlite:///twit.sqlite3"
# DATABASE_URI = "postgres://vzzdiaafvimmbi:a5930e943ae78e2c01d66d331736c6c171b8f95147ced2345ec3b68e928a3a22@ec2-3-216-89-250.compute-1.amazonaws.com:5432/d64eis3ttfk6jp"

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
