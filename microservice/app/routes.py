from flask import jsonify, request
from flask_web3 import current_web3
from app import app
from app.bdmanager import ordermanager
from app.contracts import tokencontract, ordercontract
from app import requestdata as req


order_contract_manager = ordercontract.OrderManager()

@app.route('/')
def hello_world():
    return "ok"

@app.route('/new_order', methods=['POST', 'GET'])
def new_order():
    data = request.json
    print(data['buyer'], data['seller'], data['service'], end=" ")
    order_id = ordermanager.insert_order(int(data['buyer']), int(data['seller']), int(data['service']))

    buyer_address = req.get_user_address(data['buyer'])
    seller_address = req.get_user_address(data['seller'])
    print(buyer_address, seller_address)

    buyer_address = "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1"
    seller_address = "0x8a5587F2A4B130eCf7A3c3bc1578cd6C88a51cf2"

    contract_address = order_contract_manager.deploy(buyer_address, seller_address, "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1", data['price'])
    ordermanager.add_contract_address(contract_address, order_id)
    tokencontract.approve(buyer_address, contract_address, data['price'])

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

@app.route('/confirm_supplied', methods=['GET', 'POST'])
def confirm_supplied():
    data = request.json
    seller_key = data['seller_key']
    order_id = data['order_id']
    order_state, seller, contract_address = ordermanager.get_data_to_confirm(order_id, 'seller')
    seller_address = req.get_user_address(seller)
    seller_address = "0x8a5587F2A4B130eCf7A3c3bc1578cd6C88a51cf2"

    new_order_state = order_contract_manager.confirmSupplied(order_state, seller_address, seller_key, contract_address)
    ordermanager.set_order_state(order_id, new_order_state)
    return new_order_state

@app.route('/confirm_recieved', methods=['GET', 'POST'])
def confirm_recieved():
    data = request.json
    buyer_key = data['buyer_key']
    order_id = data['order_id']
    order_state, buyer, contract_address = ordermanager.get_data_to_confirm(order_id, 'buyer')

    buyer_address = req.get_user_address(buyer)
    buyer_address = "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1"

    new_order_state = order_contract_manager.confirmRecieved(order_state, buyer_address, buyer_key, contract_address)
    ordermanager.set_order_state(order_id, new_order_state)
    return new_order_state


