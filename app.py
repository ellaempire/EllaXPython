from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('emmanuella')
    track = request.args.get('backend track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'}), 400

    # Get the current day of the week
    current_day_of_week = datetime.now().strftime('%A')

    # Get current UTC time with +/-2 minute window
    utc_now = datetime.now(pytz.utc)
    allowed_window = timedelta(minutes=2)
    min_time = utc_now - allowed_window
    max_time = utc_now + allowed_window
    current_utc_time = utc_now.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get GitHub URLs for the file being run and the full source code
    file_url = "https://github.com/ellaempire/EllaXPython/blob/main/app.py"  # Replace with your actual GitHub URL
    source_code_url = "https://github.com/ellaempire/PROJECT-1/tree/main"  # Replace with your actual GitHub URL

    # Create the response JSON
    response = {
        'slack_name': slack_name,
        'current_day_of_week': current_day_of_week,
        'current_utc_time': current_utc_time,
        'track': track,
        'github_file_url': file_url,
        'github_repo_url': source_code_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
