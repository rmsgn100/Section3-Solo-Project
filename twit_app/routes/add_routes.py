from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet
from twit_app.api import api
from embedding_as_service_client import EmbeddingClient

add_routes = Blueprint('add_routes', __name__)

en = EmbeddingClient(host='54.180.124.154', port=8989)

@add_routes.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(dict(request.form))
        result = request.form

        user = api.get_user(screen_name=result["user_name"])
        raw_tweets = api.user_timeline(screen_name=result["user_name"], count=30,
                                        include_rts=False, exclude_replies=True,
                                        tweet_mode="extended")

        new_user = User(id=user.id, username=user.screen_name, full_name=user.name, followers=user.followers_count, location=user.location)
        db.session.add(new_user)
        db.session.commit()

        tweet_texts = [_.full_text for _ in raw_tweets]

        embeddings = en.encode(texts=tweet_texts)

        for index, tweet in enumerate(raw_tweets):
            new_tweets = Tweet(id=tweet.id, text=tweet.full_text, embedding=embeddings[index], user_id=tweet.user.id)
            db.session.add(new_tweets)
     
        db.session.commit()

    data = User.query.all()
    return render_template("add.html", data=data)