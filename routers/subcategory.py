from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import subCategory, subCategorySchema
from typing import Optional


subcategory_router = APIRouter()


@subcategory_router.post('/add-subcategory')
def add_product(req: subCategorySchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_crud(req, subCategory, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')


@subcategory_router.get('/get-subcategory')
def get_subcategory(
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    try:
        result = crud.read_subcategory(category_id, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')


@subcategory_router.put('/update-subcategory')
def update_subcategory(id: int, req: subCategorySchema, db: Session = Depends(get_db)):
    try:
        result = crud.update_subcategory(id, req, db)
        result = jsonable_encoder(db.query(subCategory).all())
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@subcategory_router.delete('/delete-subcategory/{id}')
def delete_subcategory(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_subcategory(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'Successfully deleted!!!'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!') 
