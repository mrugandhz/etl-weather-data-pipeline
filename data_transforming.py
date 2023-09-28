import sqlite3

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Calculate average temperature and humidity
cursor.execute('SELECT AVG(temperature), AVG(humidity) FROM weather')
result = cursor.fetchone()
average_temperature, average_humidity = result

print(f'Average Temperature: {average_temperature:.2f}°C')
print(f'Average Humidity: {average_humidity:.2f}%')

conn.close()
