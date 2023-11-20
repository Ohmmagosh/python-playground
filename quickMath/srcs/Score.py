from typing import Iterable, Optional, Union
from rich import box
from rich.padding import PaddingDimensions
from rich.style import StyleType
from rich.table import Column, Table
from rich.console import Console, JustifyMethod
from rich.text import TextType

console = Console()

class Score:
	def __init__(self, title: str) -> None:
		self.title = title
		self.table = Table(title=f"[bold yellow]{title}")


	def	set_row_data(self, *args):
			self.table.add_row(*args)


	def set_table_header(self, data: list[dict]) -> None:
		for col in data:
			self.table.add_column(col["title"], justify=col["justify"], style=col["style"])


	def show_table(self) -> None:
		console.print(self.table)



