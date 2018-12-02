from flask import jsonify, request
from app import app
from app.bdmanager import ordermanager
from app.contracts import tokencontract, ordercontract
from app import requestdata as req
from flask_web3 import current_web3

order_contract_manager = ordercontract.OrderManager()
token_contract = tokencontract.TokenContract()

@app.route('/')
def hello_world():
    return "ok"

@app.route('/new_order', methods=['POST', 'GET'])
def new_order():
    data = request.json
    print(int(data['buyer']), int(data['seller']), int(data['service']), end=" ")
    order_id = ordermanager.insert_order(int(data['buyer']), int(data['seller']), int(data['service']))

    buyer_address = req.get_user_address(data['buyer'])
    seller_address = req.get_user_address(data['seller'])
    buyer_key = str(data['buyer_key'])
    print(buyer_address, seller_address)

    contract_address = order_contract_manager.deploy(current_web3.toChecksumAddress(buyer_address),
                                                     current_web3.toChecksumAddress(seller_address),
                                                     current_web3.toChecksumAddress("0x8a5587F2A4B130eCf7A3c3bc1578cd6C88a51cf2"),
                                                     data['price'], buyer_key)
    ordermanager.add_contract_address(contract_address, order_id)
    token_contract.approve(current_web3.toChecksumAddress(buyer_address),
                          current_web3.toChecksumAddress(contract_address),
                          data['price'], buyer_key)

    order_contract_manager.freezeTokens(current_web3.toChecksumAddress(buyer_address) ,
                                        current_web3.toChecksumAddress(contract_address),
                                        buyer_key)
    return str(order_id)

@app.route('/get_buyer_orders/<id>', methods=['GET'])
def get_buyer_orders(id):
    orders = ordermanager.get_buyer_orders(int(id))
    return jsonify(orders)


@app.route('/get_seller_orders/', methods=['GET'])
def get_seller_orders():
    seller_id = request.args.get(int('seller_id'))
    service_id = request.args.get(int('service_id'))
    orders = ordermanager.get_seller_orders(seller_id, service_id)
    return jsonify(orders)

@app.route('/confirm_supplied', methods=['GET', 'POST'])
def confirm_supplied():
    data = request.json
    seller_key = data['seller_key']
    order_id = int(data['order_id'])
    order_state, seller, contract_address = ordermanager.get_data_to_confirm_supplied(order_id)
    seller_address = req.get_user_address(seller)
    print("order state = ", order_state)

    new_order_state = order_contract_manager.confirmSupplied(order_state,
                                                             current_web3.toChecksumAddress(seller_address),
                                                             seller_key,
                                                             current_web3.toChecksumAddress(contract_address))
    ordermanager.set_order_state(order_id, new_order_state)
    print("new order state = ", new_order_state)
    return str(new_order_state)

@app.route('/confirm_recieved', methods=['GET', 'POST'])
def confirm_recieved():
    data = request.json
    buyer_key = data['buyer_key']
    order_id = data['order_id']
    order_state, buyer, contract_address = ordermanager.get_data_to_confirm_recieved(order_id)

    print("order state = ", order_state)
    buyer_address = req.get_user_address(buyer)

    new_order_state = order_contract_manager.confirmRecieved(order_state,
                                                             current_web3.toChecksumAddress(buyer_address),
                                                             buyer_key,
                                                             current_web3.toChecksumAddress(contract_address))
    ordermanager.set_order_state(order_id, new_order_state)
    print("new order state = ", new_order_state)
    return str(new_order_state)

@app.route('/balance/<id>', methods=['GET'])
def balance(id):
    address = req.get_user_address(int(id))
    milo_balance = token_contract.balance(address)
    return milo_balance