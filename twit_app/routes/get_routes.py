from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet

get_routes = Blueprint('get_routes', __name__)

@get_routes.route('/', methods=["GET", "POST"])
def index():
    tweet_data=None
    if request.method == "POST":
        print(dict(request.form))

        twit_user = request.form
        input_name = twit_user['see_tweets']

        user_info = User.query.filter_by(username=input_name).one()
        user_id = user_info.__dict__['id']

        tweet_data = Tweet.query.filter_by(user_id=user_id)

    return render_template("get.html", data=tweet_data)
