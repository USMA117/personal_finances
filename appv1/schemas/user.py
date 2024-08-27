from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints # type: ignore
from datetime import datetime

class UserBase(BaseModel):
    full_name: Annotated[str, StringConstraints(max_length=80)] 
    mail: EmailStr
    user_role: Annotated[str, StringConstraints(max_length=15)] 

class UserCreate(UserBase):
    passhash: Annotated[str, StringConstraints(max_length=40)]
    
class UserResponse(UserBase):
    user_id: str
    user_status: bool = True
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    full_name: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    mail: Optional[EmailStr] = None
    user_role: Optional[Annotated[str, StringConstraints(max_length=15)]] = None
    user_status: bool = None

class PaginatedUsersResponse(BaseModel):
    users: List[UserResponse]
    total_pages: int
    current_page: int
    page_size: int
    
class UserLoggin(UserBase):
    user_id: str
    
class PermissionsRol(BaseModel):
    module_name : str
    p_select: bool
    
class ResponseLoggin(BaseModel):
    user: UserLoggin
    permissions : List[PermissionsRol]
    access_token: str
    
# token api de correos
# mlsn.61ce6b6e8f42cb58be44017621fcc897aea1da07221fda9a3faff80514873b9b