import fitbit_data
from datetime import datetime,date
import pandas as pd
import fitbit_db
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitbit_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context(): 
    def data_insert():
        date = datetime.strptime(fitbit_data.DATE, '%Y-%m-%d').date()
        heartrate_data = fitbit_data.heart_sec
        for index, row in heartrate_data.iterrows():
            timestamp = datetime.combine(date, datetime.strptime(row['time'], '%H:%M:%S').time())  # 'time' 列にアクセス
            value = row['value']  # 'value' 列にアクセス
            user_id = 1
            heart_rate = fitbit_db.HeartRate(user_id=user_id, timestamp=timestamp, value=value)
            fitbit_db.db.session.add(heart_rate)

        # Fitbit APIから距離データを取得
        distance_data =  fitbit_data.distance_sec
        for data_point in distance_data:
            timestamp = datetime.strptime(data_point['dateTime'], '%Y-%m-%dT%H:%M:%S.%f')
            value = data_point['value']

            distance = Distance(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(distance)

        # Fitbit APIから消費カロリーデータを取得
        calorie_data = fitbit_data.calories_sec
        for data_point in calorie_data:
            timestamp = datetime.strptime(data_point['dateTime'], '%Y-%m-%dT%H:%M:%S.%f')
            value = data_point['value']

            calorie = Calorie(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(calorie)

        # Fitbit APIから歩数データを取得
        step_data = fitbit_data.steps_sec
        for data_point in step_data:
            timestamp = datetime.strptime(data_point['dateTime'], '%Y-%m-%dT%H:%M:%S.%f')
            value = data_point['value']

            step = Step(user_id=user.id, timestamp=timestamp, value=value)
            db.session.add(step)

        # データベースに全ての変更をコミット
        db.session.commit()

        return f"Fitbit data for {username} has been synchronized", 200

    data_insert()