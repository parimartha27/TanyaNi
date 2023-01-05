from . import db

from flask_login import UserMixin


class Petani(db.Model, UserMixin):
  id_petani = db.Column(db.Integer,primary_key=True)
  umur_petani = db.Column(db.Integer)