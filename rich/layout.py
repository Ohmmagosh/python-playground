from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from os import system
from time import sleep

layout = Layout()
console = Console()


def main():
	system("clear")
	layout.split_column(
		Layout(name="upper"),
		Layout(name="lower")
	)
	layout["upper"].split_row(
		Layout(name="row1"),
		Layout(name="row2")
	)
	layout["lower"].split_row(
		Layout(name="row3"),
		Layout(name="row4")
	)
	layout["lower"]["row4"].split_row(
		Layout(name="row5"),
		Layout(name="row6")
	)
	layout["lower"]["row4"]["row6"].split_column(
		Layout(name="row7"),
		Layout(name="row8")
	)
	layout["upper"]['row1'].split_row(
		Layout(name="row9"),
		Layout(name="row10")
	)
	layout["lower"]["row3"].split(
		Layout(Panel("hello")),
		Layout(Panel("world"))
	)
	console.print(layout)
	sleep(3)
	system("clear")
	console.print(layout.tree)



if __name__ == "__main__":
	main()
