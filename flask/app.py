# compose_flask/app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    if (redis.exists("vulnerabilities")):
    	return '%s vulnerabilities were found. Check Tsunami logs for details... :)' % redis.get('vulnerabilities')
    else:
        return "No vulnerabilities were found. But wait a while for the end of the first scan..."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
