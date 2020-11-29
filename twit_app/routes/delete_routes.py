from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet

delete_routes = Blueprint('delete_routes', __name__)

@delete_routes.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(dict(request.form))

        twit_user = request.form
        input_name = twit_user['delete_user']

        user_info = User.query.filter_by(username=input_name).one()
        user_id = user_info.__dict__['id']

        Tweet.query.filter_by(user_id=user_id).delete()
        User.query.filter_by(username=input_name).delete()

        db.session.commit()

    data = User.query.all()
    return render_template("delete.html", data=data)