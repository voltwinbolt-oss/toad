from flask import Flask
from flask import render_template
from datetime import datetime
from zoneinfo import ZoneInfo
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from prometheus_client import Counter

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

gandalf_requests_c = Counter('gandalf_requests', 'Number of total hits, since last restart')
colombo_requests_c = Counter('colombo_requests', 'Number of total hits, since last restart')

class colombo_time:
    def __init__(self):
        self.colombo = datetime.now(ZoneInfo('Asia/Colombo'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gandalf')
def gandalf():
    gandalf_requests_c.inc()
    return render_template('gandalf.html')

@app.route('/colombo')
def colombo():
    colombo_requests_c.inc()
    colombo_current_time = str(colombo_time().colombo)
    return colombo_current_time, render_template('colombo.html')


