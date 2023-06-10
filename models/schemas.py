from pydantic import BaseModel


class BaseSchema(BaseModel):
    name: str
    
    
class subCategorySchema(BaseSchema):
    category_id: int
    
    
class productSchema(subCategorySchema):
    description: str
    price: float 
    is_discount: bool
    size: int
    color: str 
    produced_location: str
    subcategory_id: int


class productDiscountSchema(BaseModel):
    is_discount: bool
    price: float