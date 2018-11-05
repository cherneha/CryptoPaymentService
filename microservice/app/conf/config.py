import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gWfMjs2uXjUd7EeG'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://orders_user:password@localhost:5432/orders'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
