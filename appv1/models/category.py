from sqlalchemy import SMALLINT, VARCHAR, Boolean, Column
from models.base_class import Base
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(SMALLINT(3),primary_key=True,autoincrement=True)
    
    category_name = Column(VARCHAR(50))
    category_description = Column(VARCHAR(120))
    category_status = Column(Boolean,default = True)