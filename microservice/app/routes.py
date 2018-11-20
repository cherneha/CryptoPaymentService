from flask import jsonify, request
from flask_web3 import current_web3
from app import app
from app.bdmanager import ordermanager
from app.contracts import ContractManager, ordercontract
from app import requestdata as req




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
    contract_manager = ContractManager.TokenManager()
    order_contract_manager = ordercontract.OrderManager()
    data = request.json
    print(data['buyer'], data['seller'], data['service'], end=" ")
    ordermanager.insert_order(int(data['buyer']), int(data['seller']), int(data['service']))

    buyer_address, seller_address = req.get_buyer_seller_address(data['buyer'], data['seller'])
    print(buyer_address, seller_address)

    # order_contract_manager.deploy(buyer_address, seller_address, "0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5", data['price'])

    # contract_manager.approve(data['buyer'], )
    return "ok"

# @app.route('/new_adress', methods=['POST', 'GET'])
# def new_adress():
#     # adress = current_web3.eth.accounts.create()
#     # print(adress)

@app.route('/get_buyer_orders/<id>', methods=['GET'])
def get_buyer_orders(id):
    orders = ordermanager.get_buyer_orders(id)
    return jsonify(orders)


@app.route('/get_seller_orders/', methods=['GET'])
def get_seller_orders():
    seller_id = request.args.get('seller_id')
    service_id = request.args.get('service_id')
    orders = ordermanager.get_seller_orders(seller_id, service_id)
    return jsonify(orders)






