from typing import Any
from rich.console import Console
from rich import print as rprint
from os import system
from time import sleep
from table import CTable
from random import randint

console = Console()

class App:
  def __init__(self):
    self.monney_amount = 0
    self.profit_set = list([0.03, 0.05, 0.1])

  @property
  def monney_amount(self):
    return self._monney_amount


  @monney_amount.setter
  def monney_amount(self, amount: int):
    self._monney_amount = amount

  @property
  def profit_set(self):
    return self._profit_set

  @profit_set.setter
  def profit_set(self, pset: float):
    self._profit_set = pset



  @classmethod
  def get_input(cls):
    inp = 0
    while (True):
      try:
        rprint("[yellow1]Monney amount: ", end="")
        inp = int(input())
      except (ValueError, TypeError):
        rprint("[red]Please type only integer!!!")
        cls.get_input()
      except KeyboardInterrupt:
        system("clear")
        rprint("[red]Bye Bye!!!")
        sleep(1)
        system("clear")
        break
      finally:
        cls.monney_amount = inp
        break

  @classmethod
  def profit_table(cls, instance):
    no = 0
    table = CTable("profit calclulator")
    table.add_header("No.", justify="right", style="cyan", no_wrap=True)
    table.add_header("Profit $", justify="right", style="green")
    table.add_header("Profit %", justify="right", style="yellow1")
    while (instance.monney_amount < 1000000):
        rand = randint(0, len(instance.profit_set) - 1)
        profit_rand = instance.monney_amount * instance.profit_set[rand]
        instance.monney_amount += profit_rand
        no += 1
        rand_percent_str =  f"{round(int(instance.profit_set[rand] * 100),2)} %"
        # table.add_data(str(no) , str(round(instance.monney_amount, 3)), str(round(profit_rand,2)), rand_percent_str)
    table.print()


  def run(self):
    try:
      self.get_input()
      self.profit_table(self)
    except KeyboardInterrupt:
      rprint("[red]Bye Bye!!!!")

