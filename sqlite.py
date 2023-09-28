import sqlite3
from api_code import weather_data

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create a table to store weather data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert weather data into the database
cursor.execute('''
    INSERT INTO weather (city, temperature, humidity)
    VALUES (?, ?, ?)
''', (weather_data['city'], weather_data['temperature'], weather_data['humidity']))

conn.commit()
conn.close()
