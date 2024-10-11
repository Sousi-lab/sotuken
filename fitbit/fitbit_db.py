from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from fitbit_client import FitbitClient
import fitbit_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitbit_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)
    heart_rates = db.relationship('HeartRate', backref='user', lazy=True)
    distances = db.relationship('Distance', backref='user', lazy=True)
    calories = db.relationship('Calorie', backref='user', lazy=True)
    steps = db.relationship('Step', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class HeartRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<HeartRate {self.timestamp} {self.value}>'

class Distance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Distance {self.timestamp} {self.value}>'

class Calorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Calorie {self.timestamp} {self.value}>'

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Step {self.timestamp} {self.value}>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()