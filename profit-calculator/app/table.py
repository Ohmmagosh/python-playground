from rich.table import Table
from rich.console import Console

console = Console()

class CTable:
  def __init__(self, table_name: str ):
    self.table = Table(title=table_name, style="green")

  def add_header(self, *argv, **kwargv):
    self.table.add_column(argv[0], justify=kwargv["justify"], style=kwargv["style"])

  def print(self):
    console.print(self.table)

  def add_data(self, *argv):
    self.table.add_row(*argv)

  @classmethod
  def create_table(cls, title: str):
    return Table(title=title)
