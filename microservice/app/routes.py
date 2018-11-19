from flask import jsonify, request
from flask_web3 import current_web3
from app import app
from app.bdmanager import ordermanager
from app.contracts import ContractManager

contract_manager = ContractManager.TokenManager()

@app.route('/')
def hello_world():
    # print(current_web3.eth.getBalance('0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5') / 10 ** 18)
    # # current_web3.eth.defaultAccount = '0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5'
    # token = current_web3.eth.contract(address=token_adress, abi=abi)
    # amount = token.functions.balance('0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5').call()
    # print(amount)
    # return jsonify({'data': amount})
    return "ok"

@app.route('/new_order', methods=['POST', 'GET'])
def new_order():
    data = request.json
    print(data['buyer'], data['seller'], data['service'], end=" ")
    ordermanager.insert_order(str(data['buyer']), str(data['seller']), int(data['service']))
    contract_manager.approve(data['buyer'], )
    return "ok"

# @app.route('/new_adress', methods=['POST', 'GET'])
# def new_adress():
#     # adress = current_web3.eth.accounts.create()
#     # print(adress)





