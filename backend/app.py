from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/current")
def current_data():
    data = {
        "aqi": 156,
        "pm25": 85.4,
        "pm10": 142.8,
        "no2": 45.2,
        "so2": 12.5,
        "co": 1.8,
        "o3": 68.3,
        "temperature": 28.5,
        "humidity": 62,
        "windSpeed": 12.4,
        "timestamp": "12:30 PM"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
