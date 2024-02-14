from rich.console import Console

console = Console()

class PriceRange:
  def get_input(self):
    try:
      price = int(console.input("[yellow1]Enter price: "))
      percent = int(console.input("[yellow1]Enter range: "))
    except ValueError:
      console.print("Price must be a number")
      self.get_input()
    finally:
      self.calculate_price(price, percent)


  @staticmethod
  def calculate_price(price: float, ipercent: float):
    if (price < 0 or ipercent < 0):
      raise ValueError("Price and range must be greater than 0")
    percent = price * (ipercent / 100)
    up = price + percent
    down = price - percent
    console.print(f"Price: {price}")
    console.print(f"Percent:{percent} %")
    console.print(f"Percent of price: {percent}")
    console.print(f"Up: {up}, Down: {down}")


