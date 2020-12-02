from flask import Blueprint, render_template, request
from twit_app.models import db, Trend

trend_delete_routes = Blueprint('trend_delete_routes', __name__)

@trend_delete_routes.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        input_conutry = result['delete_country']
        
        Trend.query.filter_by(country_name=input_conutry).delete()

        db.session.commit()

    data = Trend.query.all()
    return render_template("trend_delete.html", data=data)
