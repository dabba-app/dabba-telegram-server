from flask import request, Response, Blueprint, jsonify
from flask_cors import cross_origin
import controller
import logging
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

def register_endpoints(app):
    sendasync = Blueprint('sendasync', __name__, template_folder='templates')

    @cross_origin()
    @sendasync.route('/', methods=['POST'])
    def sendasync_route():
        if request.method == 'POST':
            try:
                data = controller.sendasync_controller(json.loads(request.data))
                return Response(response=json.dumps(data), mimetype='application/json')
            except Exception, e:
                logging.error(e)
                return Response(response={'error': 'Server Error, see logs'}, mimetype='application/json')

    app.register_blueprint(sendasync, url_prefix='/sendasync')