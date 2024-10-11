import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import fitbit_token
import datetime as dt

# 取得したい日付
DATE = "2024-07-10"
CLIENT_ID = '23RZ3D'
CLIENT_SECRET = '5634bd3e1e9166ad3e3239bacc51e01c'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

# ID等の設定
authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET
                             ,access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
#心拍数
data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1min') #'1sec', '1min', or '15min'
heart_sec = data_sec["activities-heart-intraday"]["dataset"]
heart_sec = pd.DataFrame.from_dict(heart_sec)
#歩数データ
data_steps = authd_client.intraday_time_series('activities/steps', DATE, detail_level='1min')
steps_sec = data_steps["activities-steps-intraday"]["dataset"]
steps_sec = pd.DataFrame.from_dict(steps_sec)
steps_sec= steps_sec[steps_sec['value'] != 0]
#カロリー消費量
data_calories = authd_client.intraday_time_series('activities/calories', DATE, detail_level='1min')
calories_sec = data_calories["activities-calories-intraday"]["dataset"]
calories_sec = pd.DataFrame.from_dict(calories_sec)
calories_sec= calories_sec[calories_sec['value'] != 0]
#移動距離
data_distance = authd_client.intraday_time_series('activities/distance', DATE, detail_level='1min')
distance_sec = data_distance["activities-distance-intraday"]["dataset"]
distance_sec = pd.DataFrame.from_dict(distance_sec)
distance_sec = distance_sec[distance_sec['value'] != 0]
#アクティブ時間
"""
data_active_minutes = authd_client.intraday_time_series('activities/activeMinutes', DATE, detail_level='1min')
active_minutes_sec = data_active_minutes["activities-activeMinutes-intraday"]["dataset"]
active_minutes_sec = pd.DataFrame.from_dict(active_minutes_sec)
"""
#睡眠データ

"""
data_sleep = authd_client.sleep(date=DATE)
data_sleep_ = data_sleep["sleep"][0]["minuteData"]
data_sleep_df = pd.DataFrame.from_dict(data_sleep_)
"""   

#体重
#weight_logs = authd_client.get_bodyweight(base_date=DATE, period='1d')
#血圧データ
"""
data_bp = authd_client.intraday_time_series('activities/bp', DATE, detail_level='1min')
bp_sec = data_bp["activities-bp-intraday"]["dataset"]
bp_sec = pd.DataFrame.from_dict(bp_sec)
"""

#アクティビティデータ
#activity_data = authd_client.activities(date=DATE)
#print(activity_data)
#print(f'血圧',bp_sec)
#print(f'心拍数',heart_sec)
#print(f'歩行数',steps_sec)
#print(f'消費カロリー',calories_sec)
#print(f'移動距離',distance_sec)
#print(f'アクティブ時間',active_minutes_sec)
#print(f'睡眠',sleep_logs)
#print(f'体重',weight_logs)



#heart_sec_last = next(reversed(heart_sec),None)

"""
last_row = heart_sec.iloc[-1]
last_value = last_row['value']
print(last_row)
"""


