from flask import jsonify, request
from flask_web3 import current_web3
from app import app
from app.bdmanager import ordermanager
from app.contracts import tokencontract, ordercontract
from app import requestdata as req




@app.route('/')
def hello_world():
    return "ok"

@app.route('/new_order', methods=['POST', 'GET'])
def new_order():
    contract_manager = tokencontract.TokenManager()
    order_contract_manager = ordercontract.OrderManager()
    data = request.json
    print(data['buyer'], data['seller'], data['service'], end=" ")
    order_id = ordermanager.insert_order(int(data['buyer']), int(data['seller']), int(data['service']))

    buyer_address, seller_address = req.get_buyer_seller_address(data['buyer'], data['seller'])
    print(buyer_address, seller_address)

    contract_address = order_contract_manager.deploy(buyer_address, seller_address, "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1", data['price'])
    ordermanager.add_contract_address(contract_address, order_id)
    contract_manager.approve(buyer_address, contract_address, data['price'])

    order_contract_manager.freezeTokens(buyer_address , contract_address)
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

