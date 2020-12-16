import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.extend([path])

from flask import Flask, Response

app = Flask(__name__)
FILE_PATH = 'covid_tracker/cases_summary.xml'


@app.route('/')
def api_root():
    return 'Welcome to Covid 19 tracker (dummy API)'


@app.route('/api/v1/summary/latest')
def get_latest():
    with open(FILE_PATH) as f:
        body = f.read()

    return Response(body, mimetype='text/xml')


if __name__ == '__main__':
    app.run(port=3000)
