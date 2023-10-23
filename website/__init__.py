from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv('.env')

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.getenv('SECRET')

  return app