from flask import Blueprint


wireless_blueprint = Blueprint('wireless', __name__, template_folder='templates')


@wireless_blueprint.route('/wireless')
def hello_world():
    return 'Wireless Dashboard'
