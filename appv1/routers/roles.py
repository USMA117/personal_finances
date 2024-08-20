from typing import List
from appv1.crud.roles import create_role_sql, get_all_roles, get_role_by_rol_name
from appv1.schemas.role import RoleCreate,RoleResponse
from fastapi import APIRouter,Depends,HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore

router = APIRouter()

@router.post("/create")
async def insert_role(role: RoleCreate, db: Session = Depends(get_db)):
    respuesta = create_role_sql(db, role)
    if respuesta:
        return {"mensaje":"Role registrado con exito"}
    else:
        return {"mensaje":"El role no se ha podido registrar con exito"}
    
@router.post("/get-role-by-name",response_model = RoleResponse)
async def get_rol_by_name(p_rol_name: str, db: Session = Depends(get_db)):
    role_buscado = get_role_by_rol_name(db, p_rol_name)
    if role_buscado is None:
        raise HTTPException(status_code=404, detail="Role no encontrado")
    return role_buscado

@router.post("/get-all_roles/",response_model = List[RoleResponse])
async def real_all_roles(db: Session = Depends(get_db)):
    roles = get_all_roles(db)
    if len(roles) == 0:
        raise HTTPException(status_code=404, detail="No hay roles")
    return roles
