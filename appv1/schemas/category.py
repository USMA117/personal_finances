from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints # type: ignore
from datetime import datetime

class CategoryBase(BaseModel):
    category_name: Annotated[str, StringConstraints(max_length=50)] 
    category_description: Annotated[str, StringConstraints(max_length=120)] 

class CategoryCreate(CategoryBase):
    category_name: Annotated[str, StringConstraints(max_length=50)] 
    category_description: Annotated[str, StringConstraints(max_length=120)] 
    category_status: bool = True
    
class CategoryResponse(CategoryBase):
    # category_id: Annotated[int, StringConstraints(max_length=3)] 
    category_status: bool = True



    # category_id SMALLINT(3) AUTO_INCREMENT PRIMARY KEY,
    # category_name VARCHAR(50),
    # category_description VARCHAR(120),
    # category_status TINYINT(1) DEFAULT 1