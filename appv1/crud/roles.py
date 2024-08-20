from http.client import HTTPException
from appv1.schemas.role import RoleCreate
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from sqlalchemy.exc import SQLAlchemyError,IntegrityError # type: ignore
from fastapi import  HTTPException # type: ignore

def create_role_sql(db: Session, role:RoleCreate):
    try:
        sql_query = text(
        "INSERT INTO roles (rol_name)"
        "VALUES (:rol_name)"
        )
        
        db.execute(sql_query, {"rol_name": role.rol_name},)
        db.commit()
        return True 
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear rol: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El rol ya existe")
            
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el rol")
    
def get_role_by_rol_name(db: Session, p_rol_name: str ):
    try:
        sql_query = text("SELECT * FROM roles WHERE rol_name = :rol_name")
        result = db.execute(sql_query, {"rol_name": p_rol_name}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar role: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar role")
    
def get_all_roles(db: Session ):
    try:
        sql_query = text("SELECT * FROM roles")
        result = db.execute(sql_query).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar roles: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar roles")