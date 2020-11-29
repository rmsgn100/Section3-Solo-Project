from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet
from sklearn.linear_model import LogisticRegression
from twit_app.routes.add_routes import en

compare_routes = Blueprint('compare_routes', __name__)

@compare_routes.route('/', methods=["GET", "POST"])
def index():
    statement = ''
    if request.method == "POST":
        print(dict(request.form))
        X = []
        y = []

        comparing = request.form
        user1 = comparing['user1']
        user2 = comparing['user2']
        tweet_to_compare = comparing['tweet_to_predict']

        user1_tweet_list = User.query.filter_by(username=user1).one().tweets
        user1_id = User.query.filter_by(username=user1).one().id
        for tweet in user1_tweet_list:
            X.append(tweet.embedding)
            y.append(user1_id)

        user2_tweet_list = User.query.filter_by(username=user2).one().tweets
        user2_id = User.query.filter_by(username=user2).one().id
        for tweet in user2_tweet_list:
            X.append(tweet.embedding)
            y.append(user2_id)

        classifier = LogisticRegression()
        classifier.fit(X, y)

        em_pred_val = en.encode(texts=[tweet_to_compare])

        pred_result = classifier.predict(em_pred_val)

        user_info = User.query.filter_by(id=int(pred_result)).one()
        user_name = user_info.__dict__['username']

        statement = f"Between '{user1}' and '{user2}', who is more likely to tweet '{tweet_to_compare}' is '{user_name}'. "
        
    data = User.query.all()
    return render_template("compare.html", data=data, statement=statement)












# def create_new_model(user1, user2, file_path):
#     X = []
#     y = []

#     user1_tweet_list = User.query.filter_by(username=user1).one().tweet
#     user1_id = User.query.filter_by(username=user1).one().id
#     for tweet in user1_tweet_list:
#         X.append(tweet.embedding)
#         y.append(user1_id)

#     user2_tweet_list = User.query.filter_by(username=user2).one().tweet
#     user2_id = User.query.filter_by(username=user2).one().id
#     for tweet in user2_tweet_list:
#         X.append(tweet.embedding)
#         y.append(user2_id)

#     classifier = LogisticRegression()
#     classifier.fit(X, y)

    

# ########################################
# def ?????

#     with open()