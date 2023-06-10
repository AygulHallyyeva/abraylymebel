from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import Base, engine
from routers import *


app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(category_router, tags=['Category'])
app.include_router(subcategory_router, tags=['Sub-Category'])
app.include_router(product_router, tags=['Product'])
app.include_router(image_router, tags=['Image'])