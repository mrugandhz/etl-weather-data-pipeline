import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Fetch temperature and humidity data for visualization
cursor.execute('SELECT timestamp, temperature, humidity FROM weather')
data = cursor.fetchall()

timestamps = [row[0] for row in data]
temperatures = [row[1] for row in data]
humidity = [row[2] for row in data]

# Create temperature and humidity plots
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, label='Temperature (°C)', color='tab:red')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.grid()

plt.twinx()
plt.plot(timestamps, humidity, label='Humidity (%)', color='tab:blue')
plt.ylabel('Humidity (%)')

plt.legend()
plt.tight_layout()
plt.show()

conn.close()
