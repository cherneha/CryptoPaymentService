from flask import Flask
from flask_web3 import FlaskWeb3
from flask_sqlalchemy import SQLAlchemy
from app.conf.config import Config


app = Flask(__name__)

app.config.from_object(Config)
app.config.update({'ETHEREUM_PROVIDER': 'http',
                   'ETHEREUM_ENDPOINT_URI': 'https://rinkeby.infura.io/v3/a5c86abf0dd042eda7954f284e278501',
                   'INFURA_API_KEY' : 'a5c86abf0dd042eda7954f284e278501'})
psqldb = SQLAlchemy(app)
wb3 = FlaskWeb3(app=app)

from app import routes

if __name__ == '__main__':
    app.run()
