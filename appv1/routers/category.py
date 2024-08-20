from typing import List
from appv1.crud.category import create_category_sql, get_all_categories, get_category_by_name
from appv1.schemas.category import CategoryCreate, CategoryResponse
from fastapi import APIRouter,Depends,HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore

router = APIRouter()

@router.post("/create")
async def insert_category(category: CategoryCreate, db: Session = Depends(get_db)):
    respuesta = create_category_sql(db, category)
    if respuesta:
        return {"mensaje":"Categoria registrado con exito"}
    else:
        return {"mensaje":"La categoria no se ha podido registrar con exito"}
    
@router.post("/get-category-by-name",response_model = CategoryResponse)
async def read_category_by_name(p_category_name: str, db: Session = Depends(get_db)):
    categoria_buscada = get_category_by_name(db, p_category_name)
    if categoria_buscada is None:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria_buscada

@router.post("/get-all_roles/",response_model = List[CategoryResponse])
async def real_all_roles(db: Session = Depends(get_db)):
    categories = get_all_categories(db)
    if len(categories) == 0:
        raise HTTPException(status_code=404, detail="No hay categorias")
    return categories
