from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz
import os

app = Flask(___name___)
IST = pytz.timezone('Asia/Kolkata')

@app.route('/calculate-time', methods=['POST'])
def calculate_time():
incoming_data = request.json or {}
current_time = datetime.now(IST)
start_iso = current_time.isoformat()
end_iso = (current_time + timedelta(hours=1)).isoformat()

return jsonify({
"results": [
{
"toolCallId": incoming_data.get("toolCallId", "test_id"),
"result": f"The current correct appointment slot is starting at {start_iso} and ending at {end_iso} IST."
}
]
})

if ___name___ == '___main___':
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)