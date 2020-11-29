from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet

update_routes = Blueprint('update_routes', __name__)

@update_routes.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(dict(request.form))

        update_user = request.form
        old_name = update_user['input_full_old']
        new_name = update_user['input_full_new']
        print(old_name)
        print(new_name)
        User.query.filter_by(full_name=old_name).update({'full_name': new_name})
        db.session.commit()
    
    data = User.query.all()
    
    return render_template("update.html", data=data)