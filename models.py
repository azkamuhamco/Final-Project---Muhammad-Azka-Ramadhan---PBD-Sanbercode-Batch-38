from constant import engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()

class Products(Base): 
    __tablename__ = 'products' 
    product_id = Column(Integer, primary_key = True) 
    product_name = Column(String(256)) 
    category = Column(String(256))
    sub_category = Column(String(256))

class Users(Base): 
    __tablename__ = 'users' 
    customer_id = Column(Integer, primary_key = True) 
    name = Column(String(256)) 
    city = Column(String(256))
    state = Column(String(256))
    postal = Column(String(5))

class PreOrders(Base):
    __tablename__ = 'preorders'
    po_id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey("users.customer_id", ondelete="cascade", onupdate="cascade")) 
    product_id = Column(Integer, ForeignKey("products.product_id", ondelete="cascade", onupdate="cascade")) 
    stock = Column(Integer) 

if __name__ == "__main__":
    Base.metadata.create_all(engine)
