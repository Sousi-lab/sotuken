import fitbit_data
import pandas as pd
import matplotlib.pyplot as plt

heart_sec_df = fitbit_data.heart_sec
heart_sec_df['time'] = pd.to_datetime(heart_sec_df['time'])

# Set 'time' as the index
heart_sec_df.set_index('time', inplace=True)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(heart_sec_df.index, heart_sec_df['value'], label='Heart Rate')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Heart Rate (bpm)')
plt.title('Heart Rate Over Time')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()