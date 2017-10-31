from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key= True)
  author = db.Column(db.String(20))
  content = db.Column(db.String(255))
  date_posted =db.Column(db.DateTime)
  category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

class Category(db.Model):
  __tablename__ = 'categories'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(140))
  pitches = db.relationship('Pitch', backref='pitch',lazy='dynamic')

class User(UserMixin,db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key= True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  password_hash = db.Column(db.String(255))
  pitches = db.relationship("Pitch", backref = 'pitch', lazy = 'dynamic')


  @property
  def password(self):
    raise AttributeError("You cannot read the password attribute")
  @password.setter
  def password(self,password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)





