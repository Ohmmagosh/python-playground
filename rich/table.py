from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="[bold yellow]Star Wars Movies")

table.add_column("Released", justify="center", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta", justify="center")
table.add_column("Box Office", justify="center", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

def	add_column(**args):
	for arg in args:
		table.add_column(arg)


def main():
	console.print(table)
	# add_column("hello", "world")


if __name__ == "__main__":
	main()
