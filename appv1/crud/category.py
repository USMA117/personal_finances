from http.client import HTTPException
from appv1.schemas.category import CategoryCreate
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from sqlalchemy.exc import SQLAlchemyError,IntegrityError # type: ignore
from fastapi import  HTTPException # type: ignore

def create_category_sql(db: Session, category:CategoryCreate):
    try:
        sql_query = text(
        "INSERT INTO category (category_name, category_description, category_status)"
        "VALUES (:category_name, :category_description, :category_status)"
        )
        params = {
            "category_name": category.category_name,
            "category_description": category.category_description,
            "category_status": category.category_status
        }
        db.execute(sql_query, params)
        db.commit()
        return True 
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear categoria: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El id de categoria ya existe")
            else:
                raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear categoria")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear categoria: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el categoria")
    
def get_category_by_name(db: Session, p_category_name: str ):
    try:
        sql_query = text("SELECT * FROM category WHERE category_name = :category_name")
        result = db.execute(sql_query, {"category_name": p_category_name}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar categoria: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categoria")
    
def get_all_categories(db: Session ):
    try:
        sql_query = text("SELECT * FROM category")
        result = db.execute(sql_query).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar categorias: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categorias")