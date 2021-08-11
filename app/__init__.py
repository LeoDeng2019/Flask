from flask import Flask

app = Flask(__name__)

from app import views
from app import admin_views

from dash_applications import create_dash_app
create_dash_app(app)