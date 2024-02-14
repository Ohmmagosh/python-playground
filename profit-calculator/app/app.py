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
    self.monney_amount: list = 0
    self.profit_set: list = list([0.03, 0.05, 0.1, -0.05])
    self.static: list = self.create_static(len(self.profit_set))

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
    self._profit_set: list = pset


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


  @staticmethod
  def random_percent(rpercent: list, rnum) -> str:
    return f"{round(int(rpercent[rnum] * 100),2)} %"

  @staticmethod
  def percent_to_str(fnum: float) -> str:
    return f"{round(int(fnum * 100),2)}"

  @classmethod
  def static_table(cls, ins):
    table  = CTable("Static")
    table.add_header("Percent", justify="center", style="cyan")
    table.add_header("Time", justify="center", style="green")
    for index in range(len(ins.profit_set)):
      table.add_data(cls.percent_to_str(ins.profit_set[index]) + " %", str(ins.static[index]))
    table.print()

  @staticmethod
  def create_static(size: int)-> list:
    li: list = []
    for i in range(size):
      li.append(0)
    return li

  @classmethod
  def profit_table(cls, ins):
    no = 0
    table = CTable("profit calclulator")
    table.add_header("No.", justify="right", style="cyan", no_wrap=True)
    table.add_header("Monney", justify="right", style="green3")
    table.add_header("Profit $", justify="right", style="green")
    table.add_header("Total $", justify="right", style="cyan")
    table.add_header("Profit %", justify="right", style="yellow1")
    while (ins.monney_amount < 1000000):
        rand = randint(0, len(ins.profit_set) - 1)
        ins.static[rand] += 1
        profit_rand = ins.monney_amount * ins.profit_set[rand]
        ins.monney_amount += profit_rand
        no += 1
        rand_percent_str = cls.random_percent(ins.profit_set, rand)
        table.add_data(
          str(no),
          str(round(ins.monney_amount - profit_rand, 2)),
          str(round(profit_rand,2)),
          str(round(ins.monney_amount, 2)),
          rand_percent_str
          )
    table.print()


  def run(self):
    try:
      self.get_input()
      self.profit_table(self)
      self.static_table(self)
    except KeyboardInterrupt:
      rprint("[red]Bye Bye!!!!")

