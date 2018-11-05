from sqlalchemy import databases
from app import psqldb


class Order(psqldb.Model):
    __tablename__ = 'Orders'

    id = psqldb.Column(psqldb.BigInteger, unique=True, primary_key=True, nullable=False, autoincrement=True)
    buyer_id = psqldb.Column(psqldb.BigInteger, nullable=False)
    seller_id = psqldb.Column(psqldb.BigInteger, nullable=False)
    service_id = psqldb.Column(psqldb.BigInteger, nullable=False)
    order_state = psqldb.Column(psqldb.Integer)
