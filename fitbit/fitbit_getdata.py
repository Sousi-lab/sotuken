from fitbit_client import FitbitClient
import fitbit_token

fitbit_client = FitbitClient()

def save_heart_rate_data(user_id, date):
    heart_data = fitbit_client.get_heart_data(date)
    for entry in heart_data:
        if entry['value'] != 0:
            heart_rate = HeartRate(user_id=user_id, timestamp=entry['time'], value=entry['value'])
            db.session.add(heart_rate)
    db.session.commit()

def save_distance_data(user_id, date):
    distance_data = fitbit_client.get_distance_data(date)
    for entry in distance_data:
        if entry['value'] != 0:
            distance = Distance(user_id=user_id, timestamp=entry['time'], value=entry['value'])
            db.session.add(distance)
    db.session.commit()

def save_calorie_data(user_id, date):
    calorie_data = fitbit_client.get_calorie_data(date)
    for entry in calorie_data:
        if entry['value'] != 0:
            calorie = Calorie(user_id=user_id, timestamp=entry['time'], value=entry['value'])
            db.session.add(calorie)
    db.session.commit()

def save_step_data(user_id, date):
    step_data = fitbit_client.get_step_data(date)
    for entry in step_data:
        if entry['value'] != 0:
            step = Step(user_id=user_id, timestamp=entry['time'], value=entry['value'])
            db.session.add(step)
    db.session.commit()
