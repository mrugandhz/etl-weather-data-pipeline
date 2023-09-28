from flask import Flask, render_template
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data from the database and perform any necessary processing
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp, temperature, humidity FROM weather')
    data = cursor.fetchall()
    conn.close()

    timestamps = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    humidity = [row[2] for row in data]

    # Create a temperature and humidity plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('Temperature (°C)', color='tab:red')
    ax1.plot(timestamps, temperatures, label='Temperature (°C)', color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Humidity (%)', color='tab:blue')
    ax2.plot(timestamps, humidity, label='Humidity (%)', color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    plt.title('Temperature and Humidity Over Time')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data_uri = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return render_template('index.html', plot_data=plot_data_uri)

if __name__ == '__main__':
    app.run(debug=True)
