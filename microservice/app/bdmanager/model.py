from app import psqldb


class Order(psqldb.Model):
    __tablename__ = 'Orders'

    id = psqldb.Column(psqldb.BigInteger, unique=True, primary_key=True, nullable=False, autoincrement=True)
    buyer = psqldb.Column(psqldb.BigInteger, nullable=False)
    seller = psqldb.Column(psqldb.BigInteger, nullable=False)
    service = psqldb.Column(psqldb.BigInteger, nullable=False)
    order_state = psqldb.Column(psqldb.Integer)
    order_date = psqldb.Column(psqldb.DateTime, default=psqldb.func.now(), nullable=False)
    contract_adress = psqldb.Column(psqldb.String, nullable=True)


    def __init__(self, buyer_id, seller_id, service_id, order_state):
        self.buyer = buyer_id
        self.seller = seller_id
        self.service = service_id
        self.order_state = order_state
