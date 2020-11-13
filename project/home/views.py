from flask import Blueprint
from flask import request
from pprint import pprint


home_blueprint = Blueprint('home', __name__, template_folder='templates')

VALIDATOR = os.environ['VALIDATOR']
LOCSECRETKEY = os.environ['LOCSECRETKEY']


def save_data(data):
    print("---- SAVING Location DATA ----")
    # CHANGE ME - send 'data' to a database or storage system
    pprint(data, indent=1)


@home_blueprint.route('/', methods=['GET'])
def get_validator():
    print("validator sent to: ", request.environ['REMOTE_ADDR'])
    return VALIDATOR


@home_blueprint.route('/', methods=['POST'])
def posted_scanning_api_json():
    if not request.json or not 'data' in request.json:
        return "invalid data", 400

    api_data = request.json

    print("Received POST from ", request.environ['REMOTE_ADDR'])

    # Verify secret
    if api_data['secret'] != LOCSECRETKEY:
        print("secret invalid:", api_data['secret'])
        return "invalid secret", 403
    else:
        print("secret verified: ", api_data['secret'])

    # Do something with data (commit to database)
    save_data(api_data)

    # Return success message
    return "Location Scanning POST Received"
