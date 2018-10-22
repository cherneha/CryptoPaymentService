from flask import Flask, jsonify
from flask_web3 import FlaskWeb3, current_web3

app = Flask(__name__)
app.config.update({'ETHEREUM_PROVIDER': 'http',
                   'ETHEREUM_ENDPOINT_URI': 'https://rinkeby.infura.io/v3/00bd814d42c342c0a78fcf6266b269c5',
                   'INFURA_API_KEY' : '00bd814d42c342c0a78fcf6266b269c5'})
web3 = FlaskWeb3(app=app)

@app.route('/')
def hello_world():
    return jsonify({'data': current_web3.eth.blockNumber})


if __name__ == '__main__':
    app.run()
