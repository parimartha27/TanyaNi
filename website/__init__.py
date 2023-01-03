from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'tanyaNi.db'

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lancarkanlah project kami ya Tuhan'
  app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
  db.init_app(app)

  
  from .views import views
  app.register_blueprint(views,url_prefix='/')
  return app