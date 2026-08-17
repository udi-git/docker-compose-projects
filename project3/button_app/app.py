from flask import Flask , render_template , redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/press', methods=['POST'])
def press_button():
    url = "http://clock_app:5001/update_time"
    requests.post(url)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


