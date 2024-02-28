from pydantic import BaseModel, field_validator

class Item(BaseModel):
  name: str
  description: str = None
  price: float
  tax: float = None


class Item2(BaseModel):
  name: str
  description: str = None
  price: float
  tax: float = None

  @field_validator("price")
  def price_must_be_positive(cls, v):
    if v < 0:
      raise ValueError("must be greater than 0")
    return v

  @field_validator("name")
  def name_hello(cls, v):
    if v == 'hello':
      v = 'world'
    return v
