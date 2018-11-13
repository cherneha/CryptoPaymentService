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
        return False
    return True