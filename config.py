import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/clon_point_credit'
    SQLALCHEMY_TRACK_MODIFICATIONS = False