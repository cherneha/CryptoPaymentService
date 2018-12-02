from app import psqldb
from app.bdmanager.model import Order

def insert_order(buyer, seller, service):
    order = Order(buyer,
                  seller,
                  service,
                  1)
    try:
        psqldb.session.add(order)
    except:
        print("Error occured when inserting new order.")
        return -1
    try:
        psqldb.session.commit()
    except Exception as e:
        print(e)
        print("Error while commiting to DB.")
        return -1
    return order.id

def add_contract_address(address, id):
    order = Order.query.filter_by(id=id).first()
    order.contract_adress = address
    try:
        psqldb.session.commit()
    except Exception as e:
        print(e)
        print("Error while commiting to DB.")


def get_buyer_orders(buyer_id):
    res = Order.query.filter_by(buyer=buyer_id)
    res_json = {}
    res_json['orders'] = []
    for r in res:
        order = {}
        order['id'] = r.service
        order['date'] = r.date
        order['order_state'] = r.order_state
        order['seller_id'] = r.seller
        res_json['orders'] = res_json['orders'].append(order)
    print(res_json)
    return res_json

def get_seller_orders(seller_id, service_id):
    res = Order.query.filter_by(seller=seller_id, service=service_id)
    res_json = {}
    res_json['orders'] = []
    for r in res:
        order = {}
        order['buyer'] = r.buyer
        order['date'] = r.date
        res_json['orders'] = res_json['orders'].append(order)
    print(res_json)
    return res_json

def get_contract_address(order_id):
    res = Order.query.filter_by(id=order_id).first()
    return res.contract_adress


def get_data_to_confirm_recieved(order_id):
    res = Order.query.filter_by(id=order_id).first()
    return res.order_state, res.buyer, res.contract_adress

def get_data_to_confirm_supplied(order_id):
    res = Order.query.filter_by(id=order_id).first()
    print(res.order_state, res.contract_adress, res.id, res.seller, res.buyer, res.service, res.order_date, end=',')
    return res.order_state, res.seller, res.contract_adress


def set_order_state(order_id, new_state):
    res = Order.query.filter_by(id=order_id).first()
    res.order_state = new_state
    try:
        psqldb.session.commit()
    except Exception as e:
        print(e)
        print("Error while commiting to DB.")

