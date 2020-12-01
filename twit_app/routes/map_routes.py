from flask import Blueprint, render_template, request
from twit_app.models import db, User, Tweet
import folium
from geopy.geocoders import Nominatim

map_routes = Blueprint('map_routes', __name__)

@map_routes.route('/', methods=["GET", "POST"])
def index():
    lat = ''
    lon = ''
    if request.method == "POST":
        print(dict(request.form))

        twit_user = request.form
        print(twit_user)
        input_name = twit_user['find_location']
        print(input_name)

        user_info = User.query.filter_by(username=input_name).one()
        user_location = user_info.__dict__['location']



        locator = Nominatim(user_agent="myGeocoder")
        location = locator.geocode(user_location)

        lat = location.latitude
        lon = location.longitude
    return render_template("map.html", lat=lat, lon=lon)