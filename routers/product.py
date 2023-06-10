from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import productSchema, Product, productDiscountSchema
from typing import Optional

product_router = APIRouter()

@product_router.post('/add-product')
def add_product(req: productSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_crud(req, Product, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')


@product_router.get('/get-product')
def get_product(
    category_id: Optional[int] = None,
    subcategory_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    try:
        result = crud.read_product(category_id, subcategory_id, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    

@product_router.put('/update-product')
def update_product(id: int, req: productDiscountSchema, db: Session = Depends(get_db)):
    try:
        result = crud.update_product(id, req, db)
        result = jsonable_encoder(db.query(Product).all())
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@product_router.delete('/delete-product/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_product(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'Successfully deleted!!!'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@product_router.get('/get-discount-product')
def get_discount_product(
    db: Session = Depends(get_db)
):
    try:
        result = crud.read_discount_product(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')