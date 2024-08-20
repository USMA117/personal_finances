import enum
from typing import Annotated
from pydantic import BaseModel, StringConstraints # type: ignore

class rol_type(enum.Enum):
    admin = "Admin"
    cliente = "Cliente"
    super_admin = "SuperAdmin"
    
    
class RoleBase(BaseModel):
    rol_name: Annotated[str, StringConstraints(max_length=15)] 

class RoleCreate(RoleBase):
    rol_name: Annotated[str, StringConstraints(max_length=15)] 

class RoleResponse(RoleBase):
    rol_name: Annotated[str, StringConstraints(max_length=15)] 