from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db.videos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# models will map to tables in the database
class Customer(db.Model):
    pass


class Order(db.Model):
    pass


class Product(db.Model):
    pass
