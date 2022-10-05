from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.DevConfig')

CORS(app)

# BluePrints
# from app.auth_api.views import auth_bp
# app.register_blueprint(auth_bp, url_prefix='/auth')


from app import views
