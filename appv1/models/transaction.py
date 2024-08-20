from sqlalchemy import CHAR, FLOAT, INT, SMALLINT, VARCHAR, Column, Date, ForeignKey
from models.base_class import Base
from sqlalchemy.orm import relationship
import enum

class TransactionType(enum.Enum):
    revenue = "revenue"
    expenses = "expenses"

class Transaction(Base):
    __tablename__ = 'transactions'
    transactions_id = Column(INT,primary_key=True,autoincrement=True)
    user_id = Column(CHAR(30),ForeignKey('users,user.id'))
    category_id = Column(SMALLINT(3),ForeignKey('category,category.category_id'))
    amount = Column(FLOAT(10,2))
    t_description = Column(VARCHAR(120))
    t_type = Column(enum.Enum(TransactionType))
    t_date = Column(Date)

    user = relationship("User")
    category = relationship("Category")