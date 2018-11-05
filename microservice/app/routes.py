from flask import jsonify, request
from flask_web3 import current_web3
from app import app
from app.bdmanager.model import Order

@app.route('/')
def hello_world():
    token_adress = '0xfa8b724558412CD5f2E07cAF2337885dA13864D5'
    abi = '[{"constant":true,"inputs":[],"name":"supply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},' \
          '{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},' \
          '{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve",' \
          '"outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"a","type":"uint256"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},' \
          '{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":' \
          '[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,' \
          '"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"",' \
          '"type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to",' \
          '"type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],' \
          '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner",' \
          '"type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],' \
          '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],' \
          '"name":"balance","outputs":[{"name":"accountBalance","type":"uint256"}],"payable":false,"stateMutability":"view",' \
          '"type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'

    print(current_web3.eth.getBalance('0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5') / 10 ** 18)
    # current_web3.eth.defaultAccount = '0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5'
    token = current_web3.eth.contract(address=token_adress, abi=abi)
    amount = token.functions.balance('0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5').call()
    print(amount)
    return jsonify({'data': amount})

@app.route('/new_order', methods=['POST', 'GET'])
def new_order():
    data = request.json
    order = Order(data['buyer'], data['seller'], data['service'], data['order'])



