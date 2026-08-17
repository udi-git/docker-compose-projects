import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

israel_tz = datetime.timezone(datetime.timedelta(hours=3))

now = datetime.datetime.now(israel_tz)

@app.route('/')
def time():
    time_str = now.strftime("%H:%M:%S")
    return render_template('index.html', time=time_str)

@app.route('/update_time', methods=['POST'])
def update_time():
    global now
    now -= datetime.timedelta(minutes=1)
    time_str = now.strftime("%H:%M:%S")
    return jsonify ({"status": "success", "new_time": time_str})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
