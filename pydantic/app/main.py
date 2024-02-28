
from pydantic import ValidationError
from rich import print
from models import Item, Item2
from data import data_sample

def main():
  data_sample_success, data_sample_error, data_sample_exclude, data_sample_field, data_sample_field_error = data_sample()

  try:
    item = Item(**data_sample_success)
    print(item.model_dump())
  except ValidationError as e:
    print("Error: ", e)

  try:
    item2 = Item(**data_sample_error)
    print(item2.model_dump())
  except ValidationError as e:
    print("Error: ", e)

  try:
    item3 = Item(**data_sample_exclude)
    print("exclude unset")
    print(item3.model_dump())
    print("exclude tax")
    print(item3.model_dump(exclude={"tax"}))
  except ValidationError as e:
    print("Error: ", e)

  try:
    item4 = Item2(**data_sample_field)
    print(item4.model_dump())
  except ValidationError as e:
    print("Error: ", e)

  try:
    item5 = Item2(**data_sample_field_error)
    print(item5.model_dump())
  except ValidationError as e:
    print("Error: ", e)

if __name__ == "__main__":
  main()
