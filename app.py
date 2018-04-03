import os
import json
import logging
import threading
from flask import (
    Flask,
    request,
    redirect,
    jsonify
)
from flask_cors import CORS
from api import routes

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

try:
    with open(os.path.dirname(os.path.realpath(__file__)) + '/config.json') as json_config_file:
        config = json.load(json_config_file)

    for k, v in config.iteritems():
        os.environ[k] = v

except Exception as e:
    logging.warning(e)


app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'dabba-telegram root'})

routes.register_endpoints(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 8000)), host=os.getenv('HOST', '0.0.0.0'), use_reloader=False)
