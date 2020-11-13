from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# import blueprints

from project.wireless.views import wireless_blueprint
from project.home.views import home_blueprint


app.register_blueprint(wireless_blueprint)
app.register_blueprint(home_blueprint)
