from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import pandas as pd
import fitbit_data
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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

with app.app_context(): 
    def data_insert():
        date = datetime.strptime(fitbit_data.DATE, '%Y-%m-%d').date()
        heartrate_data = fitbit_data.heart_sec
        for index, row in heartrate_data.iterrows():
            timestamp = datetime.combine(date, datetime.strptime(row['time'], '%H:%M:%S').time())  # 'time' 列にアクセス
            value = row['value']  # 'value' 列にアクセス
            user_id = 1
            heart_rate = HeartRate(user_id=user_id, timestamp=timestamp, value=value)
            db.session.add(heart_rate)

        # Fitbit APIから距離データを取得
        distance_data =  fitbit_data.distance_sec
        for data_point in distance_data:
            timestamp = datetime.combine(date, datetime.strptime(row['time'], '%H:%M:%S').time())
            value = data_point['value']

            distance = Distance(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(distance)

        # Fitbit APIから消費カロリーデータを取得
        calorie_data = fitbit_data.calories_sec
        for data_point in calorie_data:
            timestamp = datetime.combine(date, datetime.strptime(row['time'], '%H:%M:%S').time())
            value = data_point['value']

            calorie = Calorie(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(calorie)

        # Fitbit APIから歩数データを取得
        step_data = fitbit_data.steps_sec
        for data_point in step_data:
            timestamp = datetime.combine(date, datetime.strptime(row['time'], '%H:%M:%S').time())
            value = data_point['value']

            step = Step(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(step)

        # データベースに全ての変更をコミット
        db.session.commit()

        return f"データ挿入完了"

    data_insert()

@app.route('/')
def index():
    heart_sec = fitbit_data.heart_sec
    last_row = heart_sec.iloc[-1]
    last_value = last_row['value']
    return render_template('index.html',heart_sec=last_value)

@app.route('/heart', methods=['GET','POST'])
def heart():
    df = pd.DataFrame(heart_sec)
    start_date = request.form.get('start_date',df['time'].min().strftime('%Y-%m-%d'))
    end_date = request.form.get('end_date',df['time'].min().strftime('%Y-%m-%d'))

    

    return render_template('index.html',heart_sec=last_value)

if __name__ == '__main__':
    app.run(debug=True)