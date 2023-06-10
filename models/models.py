from sqlalchemy import *
from sqlalchemy.orm import *
from db import Base
from datetime import *


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    subcategory = relationship('subCategory', back_populates='category')
    product = relationship('Product', back_populates='category')
    
    
    
class subCategory(Base):
    __tablename__ = 'sub_category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    category = relationship('Category', back_populates='subcategory')
    product = relationship('Product', back_populates='subcategory')
    subcategory_image = relationship('subCategoryImage', back_populates='subcategory')
    

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    is_discount = Column(Boolean, default=False)
    size = Column(Integer)
    color = Column(String)
    produced_location = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    subcategory_id = Column(Integer, ForeignKey('sub_category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    category    = relationship('Category', back_populates='product')
    subcategory = relationship('subCategory', back_populates='product')
    product_image       = relationship('productImage', back_populates='product')
    
    
    
class productImage(Base):
    __tablename__ = 'product_image'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    product = relationship('Product', back_populates='product_image')
    

class subCategoryImage(Base):
    __tablename__ = 'subcategory_image'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    subcategory_id = Column(Integer, ForeignKey('sub_category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    subcategory = relationship('subCategory', back_populates='subcategory_image')