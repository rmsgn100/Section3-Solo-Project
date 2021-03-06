from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import pickle
import pickle5 as pickle

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String)
    full_name = db.Column(db.String)
    followers = db.Column(db.Integer)
    location = db.Column(db.String)

    def __repr__(self):
        return "< User {} {} >".format(self.id, self.username)


class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String)
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))

    user=db.relationship("User", backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return f"< Tweet {self.id} {self.text} >"


# class Country(db.Model):
#     woeid = db.Column(db.BigInteger, primary_key=True)
#     country_name = db.Column(db.String, db.ForeignKey("user.location"))

#     def __repr__(self):
#         return f"< Country {self.woeid} {self.country_name} >"


class Trend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic = db.Column(db.String)
    woeid = db.Column(db.BigInteger)
    country_name = db.Column(db.String)

    def __repr__(self):
        return f"< Trend {self.id} {self.topic} {self.woeid} >"


def parse_records(db_records):
    parsed_list = []
    for record in db_records:
        parsed_record = record.__dict__
        print(parsed_record)
        del parsed_record["_sa_instance_state"]
        parsed_list.append(parsed_record)
    return parsed_list
