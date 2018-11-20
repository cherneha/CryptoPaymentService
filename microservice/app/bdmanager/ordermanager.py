from app import psqldb
from app.bdmanager.model import Order

def insert_order(buyer, seller, service):
    order = Order(buyer,
                  seller,
                  service,
                  0)
    try:
        psqldb.session.add(order)
    except:
        print("Error occured when inserting new order.")
        return False
    try:
        psqldb.session.commit()
    except Exception as e:
        print(e)
        print("Error while commiting to DB.")
        return False
    return True

def get_buyer_orders(buyer_id):
    res = Order.query.filter_by(buyer=buyer_id)
    res_json = {}
    res_json['orders'] = []
    for r in res:
        order = {}
        order['id'] = r.service
        order['date'] = r.date
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
