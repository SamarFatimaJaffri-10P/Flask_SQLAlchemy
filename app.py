from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_sqlalchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# models will map to tables in the database
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)            # primary key
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    orders = db.relationship('Order', backref='customer')   # backref means back reference


# association table
order_product = db.Table('order_product',
                         db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
                         db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
                         )


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)            # primary key
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ship_date = db.Column(db.DateTime)
    deliver_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    products = db.relationship('Product', secondary=order_product)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)            # primary key
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
