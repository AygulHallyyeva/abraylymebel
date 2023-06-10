from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud

image_router = APIRouter()

# upload and delete images of products

@image_router.post('/upload-product-image')
def uplaod_product_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_product_img(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    
    
@image_router.delete('/delete-product-image/{id}')
def delete_product_image(id: int, db: Session = Depends(get_db)):
    try:  
        result = crud.delete_product_img(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"result": 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})


# upload and delete images of subcategories

@image_router.post('/upload-subcategory-image')
def uplaod_subcategory_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_subcategory_img(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    
    
@image_router.delete('/delete-subcategory-image/{id}')
def delete_subcategory_image(id: int, db: Session = Depends(get_db)):
    try:  
        result = crud.delete_subcategory_img(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"result": 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})
    
    
    

    