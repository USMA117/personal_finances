
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from sqlalchemy.exc import SQLAlchemyError # type: ignore
from fastapi import  HTTPException # type: ignore


# Consultar permisos de un rol por cada modulo
def get_permissions(db: Session, rol: str, module: str):
    try:
        sql = text("SELECT p_select, p_insert, p_update, p_delete FROM permissions WHERE rol_name = :rol AND module_name = :module ")
        result = db.execute(sql, {"rol": rol, "module":module}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar email por correo: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar email por correo")
    

# Consultar todos los permisos de un rol por cada modulo
def get_all_permissions(db: Session, rol: str):
    try:
        sql = text("SELECT module_name, p_select FROM permissions WHERE rol_name = :rol ")
        result = db.execute(sql, {"rol": rol}).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar email por correo: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar email por correo")