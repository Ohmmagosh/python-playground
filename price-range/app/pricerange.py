from rich.console import Console
import sys

console = Console()

class Input:
  def __init__(self, price: float = 0, percent: float = 0):
    self.price = price
    self.percent = percent

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    self._price = value

  @property
  def percent(self):
    return self._percent

  @percent.setter
  def percent(self, value):
    self._percent = value

class PriceRange:
  @classmethod
  def get_input(cls) -> Input:
    try:
      price = float(console.input("[yellow1]Enter price: "))
      percent = float(console.input("[yellow1]Enter percent: "))
      return Input(price, percent)
    except ValueError:
      console.print("Price must be a number")
      cls.get_input()


  @staticmethod
  def calculate_price(price: float, ipercent: float):
    if (price <= 0 or ipercent <= 0):
      raise ValueError("Price and range must be greater than 0")
    percent = price * (ipercent / 100)
    up = f"[green]{price + percent}[bright_white]"
    down = f"[red]{price - percent}[bright_white]"
    console.print(f"Price: {price}")
    console.print(f"Percent:{ipercent} %")
    console.print(f"Percent of price: {percent} $")
    console.print(f"Price Up: {up},Price Down: {down}")

  @staticmethod
  def print_error(msg: str):
    console.print(f"[red]Error: {msg}")


