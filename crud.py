from fastapi import Depends
from db import get_db
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy import or_, and_
from models import *
from upload_depends import upload_image, delete_uploaded_image


def create_crud(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_category(db: Session):
    result = db.query(Category).options(joinedload(Category.subcategory)).all()
    return result


def update_category(id, req, db: Session):
    new_update = db.query(Category).filter(Category.id == id)\
            .update(
                {
                    Product.name: req.name
                },synchronize_session=False
        )
    db.commit()
    return new_update


# subcategory functions

def read_subcategory(category_id, db: Session):
    result = db.query(
        subCategory,
        Category.name.label('categoryName'),
    ).options(joinedload(subCategory.subcategory_image).load_only('img'))\
    .join(Category, Category.id == subCategory.category_id)\
    
    if category_id:
        result = result.filter(subCategory.category_id == category_id)
    result = result.all()
    return result


def update_subcategory(id, req, db: Session):
    new_update = db.query(subCategory).filter(subCategory.id == id)\
            .update(
                {
                    subCategory.name: req.name,
                    subCategory.category_id: req.category_id
                },synchronize_session=False
        )
    db.commit()
    return new_update


def delete_subcategory(id, db: Session):
    db.query(subCategoryImage).filter(subCategoryImage.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    new_delete = db.query(subCategory).filter(subCategory.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    return True


# Product functions

def read_product(category_id, subcategory_id, db: Session):
    result = db.query(
        Product,
        Category.name.label('categoryName'),
        subCategory.name.label('subCategoryName'),
    ).options(joinedload(Product.product_image).load_only('img'))\
    .join(Category, Category.id == Product.category_id)\
    .join(subCategory, subCategory.id == Product.subcategory_id)
    
    if category_id:
        result = result.filter(Product.category_id == category_id)
    if subcategory_id:
        result = result.filter(Product.subcategory_id == subcategory_id)
    result = result.all()
    return result


def update_product(id, req, db: Session):
    new_update = db.query(Product).filter(Product.id == id)\
            .update(
                {
                    Product.is_discount: req.is_discount,
                    Product.price: req.price
                },synchronize_session=False
        )
    db.commit()
    return new_update


def delete_product(id, db: Session):
    db.query(productImage).filter(productImage.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    new_delete = db.query(Product).filter(Product.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    return True


def read_discount_product(db: Session):
    result = db.query(Product).filter(Product.is_discount == True).all()
    return result


# uploading and deleting images

def create_product_img(id, file, db: Session):
    uploaded_file_name = upload_image('product', file)
    new_add = productImage(
        img = uploaded_file_name,
        product_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def delete_product_img(id, db: Session):
    image = db.query(productImage).filter(productImage.id == id).first()
    if image.img:
        delete_uploaded_image(image_name=image.img)
        db.query(productImage).filter(productImage.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True


def create_subcategory_img(id, file, db: Session):
    uploaded_file_name = upload_image('subcategory', file)
    new_add = subCategoryImage(
        img = uploaded_file_name,
        subcategory_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def delete_subcategory_img(id, db: Session):
    image = db.query(subCategoryImage).filter(subCategoryImage.id == id).first()
    if image.img:
        delete_uploaded_image(image_name=image.img)
        db.query(subCategoryImage).filter(subCategoryImage.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True