import os

class Config:
  SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://puppah:zanpakutou@localhost/pitch_hub'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY=os.environ.get('SECRET_KEY')
class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}