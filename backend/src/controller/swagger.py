from flask import Blueprint, send_file


swagger = Blueprint('swagger', __name__)

@swagger.route("/swagger")
def get_swagger():
    return send_file('openapi.yaml')
