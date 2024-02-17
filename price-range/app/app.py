from pricerange import PriceRange, Input
from os import system
from rich.console import Console
from time import sleep

console = Console()

class App(PriceRange):
  def run(self):
    try:
      price_percent: Input = self.get_input()
      self.calculate_price(price_percent.price, price_percent.percent)
    except KeyboardInterrupt:
      system("clear")
      self.print_error("Exiting...")
      sleep(1)
      system("clear")
      exit(0)
    except Exception as e:
      print(e)

