import fitbit_data
import pandas as pd
import matplotlib.pyplot as plt

distance_sec_df = fitbit_data.distance_sec
distance_sec_df['time'] = pd.to_datetime(distance_sec_df['time'])
distance_sum = distance_sec_df['value'].sum()

# Set 'time' as the index
distance_sec_df.set_index('time', inplace=True)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(distance_sec_df.index, distance_sec_df['value'], label='distance')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('distance')
plt.title('distance Over')
plt.legend()
plt.grid(True)
plt.figtext(0.15, 0.9, f'Total distance: {distance_sum}', fontsize=12, ha='left', va='center')

# Show the plot
plt.show()