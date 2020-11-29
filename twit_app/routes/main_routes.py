from flask import Blueprint, render_template, jsonify
from twit_app.models import User, parse_records

main_routes = Blueprint('main_routes', __name__)

# '/'
@main_routes.route('/')
def index():
    data = User.query.all()
    return render_template("index.html", data=data)

# '/add.json
@main_routes.route('/add.json')
def json_data():
    raw_data = User.query.all()
    parsed_data = parse_records(raw_data)
    
    return jsonify(parsed_data)