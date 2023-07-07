import json
import urllib.parse
import urllib.request

from urllib.error import HTTPError

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_request():
    json_data = request.get_json()

    if json_data['function'] == 'get_weather':
        location = urllib.parse.quote(json_data['argument']['location'])
        url = f"https://api.weatherapi.com/v1/current.json?key={YOUR_API_KEY}&q={location}&aqi=no"

        try:
            with urllib.request.urlopen(url) as response:
                weather_data = json.loads(response.read().decode())

            response_text = f"{weather_data['current']['condition']['text']} {weather_data['current']['temp_f']}F degrees."
        except HTTPError:
            response_text = "Error retrieving weather information."

    elif json_data['function'] == 'get_world_time':
        location = urllib.parse.quote(json_data['argument'])
        url = f"http://api.weatherapi.com/v1/timezone.json?key={YOUR_API_KEY}&q={location}"

        try:
            with urllib.request.urlopen(url) as response:
                time_data = json.loads(response.read().decode())

            response_text = f"<say-as interpret-as='time' format='hm12'>{time_data['location']['localtime']}</say-as>"
        except HTTPError:
            response_text = "Error retrieving world time information."

    else:
        response_text = "Unknown function."

    response = {
        'response': response_text
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
