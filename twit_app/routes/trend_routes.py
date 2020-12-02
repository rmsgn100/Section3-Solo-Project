from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet, Trend
from twit_app.api import api
import json

trend_routes = Blueprint('trend_routes', __name__)

@trend_routes.route('/', methods=["GET", "POST"])
def index():
    trend_list = []
    # Korea = 1130853
    # USA = 2352824
    # Japan = 1110809
    # UK = 12723
    # France = 580778
    # Germany = 638242
    # Spain = 753692
    # Russia = 1997422
    # Italy = 711080

    if request.method == "POST":
        print(dict(request.form))

        result = request.form
        input_contry = result['country_name']
        
        if input_contry == 'Korea':
            WOE_ID = 1130853
            korea_trends = api.trends_place(WOE_ID)
            print(korea_trends)
            trends = json.loads(json.dumps(korea_trends, indent=1))
        
        elif input_contry == 'USA':
            WOE_ID = 2352824
            usa_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(usa_trends, indent=1))

        elif input_contry == 'Japan':
            WOE_ID = 1110809
            japan_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(japan_trends, indent=1))

        elif input_contry == 'UK':
            WOE_ID = 12723
            uk_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(uk_trends, indent=1))

        elif input_contry == 'France':
            WOE_ID = 580778
            france_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(france_trends, indent=1))

        elif input_contry == 'Germany':
            WOE_ID = 638242
            germany_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(germany_trends, indent=1))
        
        elif input_contry == 'Spain':
            WOE_ID = 753692
            spain_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(spain_trends, indent=1))

        elif input_contry == 'Russia':
            WOE_ID = 1997422
            russia_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(russia_trends, indent=1))

        elif input_contry == 'Italy':
            WOE_ID = 711080
            italy_trends = api.trends_place(WOE_ID)
            trends = json.loads(json.dumps(italy_trends, indent=1))


        for trend in trends[0]["trends"][:10]:
            print (trend["name"])
            trend_list.append(trend["name"])
            new_trend = Trend(topic=trend["name"], woeid=WOE_ID, country_name=input_contry)
            db.session.add(new_trend)

        db.session.commit()


    return render_template("trend.html", trend_list=trend_list)