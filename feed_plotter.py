import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz

# Import CSV files
channel1_df = pd.read_csv('/Users/God/Desktop/iot_assg_3/channel1_feed.csv')
channel2_df = pd.read_csv('/Users/God/Desktop/iot_assg_3/channel2_feed.csv')

# Convert timestamp column to datetime objects
channel1_df['created_at'] = pd.to_datetime(channel1_df['created_at'])
channel2_df['created_at'] = pd.to_datetime(channel2_df['created_at'])

# Make current_time timezone-aware
current_time = datetime.now() - timedelta(hours=5)
current_time = current_time.replace(tzinfo=pytz.UTC)  # Make current_time timezone-aware

# Adjust timestamps to current system time - 5 hours
channel1_df['created_at'] = channel1_df['created_at'] + (current_time - channel1_df['created_at'].max())
channel2_df['created_at'] = channel2_df['created_at'] + (current_time - channel2_df['created_at'].max())

# Plot visualization graphs
plt.figure(figsize=(12, 8))
#print(channel1_df)
# Temperature vs. Time
plt.subplot(3, 1, 1)
plt.plot(channel1_df['created_at'], channel1_df['field1'], label='Channel 1 Temperature', color='blue')
plt.plot(channel2_df['created_at'], channel2_df['field1'], label='Channel 2 Temperature', color='red')
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Temperature vs. Time')
plt.legend()

# Humidity vs. Time
plt.subplot(3, 1, 2)
plt.plot(channel1_df['created_at'], channel1_df['field2'], label='Channel 1 Humidity', color='green')
plt.plot(channel2_df['created_at'], channel2_df['field2'], label='Channel 2 Humidity', color='orange')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity vs. Time')
plt.legend()

# CO2 vs. Time
plt.subplot(3, 1, 3)
plt.plot(channel1_df['created_at'], channel1_df['field3'], label='Channel 1 CO2', color='purple')
plt.plot(channel2_df['created_at'], channel2_df['field3'], label='Channel 2 CO2', color='brown')
plt.xlabel('Time')
plt.ylabel('CO2 (ppm)')
plt.title('CO2 vs. Time')
plt.legend()

plt.tight_layout()
plt.show()