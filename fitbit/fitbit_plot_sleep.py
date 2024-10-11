
import matplotlib.pyplot as plt
import fitbit_data
import pandas as pd
import matplotlib.dates as mdates


sleep_df = fitbit_data.data_sleep_df
print(sleep_df)
sleep_df['value'] = sleep_df['value'].astype(int)
sleep_df['dateTime'] = pd.to_datetime(sleep_df['dateTime'], format='%H:%M:%S')
sleep_df.set_index('dateTime', inplace=True)


# Plotting the data
fig, ax = plt.subplots(figsize=(18, 6))
ax.plot(sleep_df.index, sleep_df['value'], label='Sleep Value')
locator = mdates.AutoDateLocator()
formatter = mdates.DateFormatter("%H:%M")

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Sleep Data Over Time')
plt.legend()
plt.grid(True)
fig.autofmt_xdate(rotation=90, ha="center")

# Show the plot
plt.show()
