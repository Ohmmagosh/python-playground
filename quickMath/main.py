import random
from time import sleep
from os import system
from QuickMath import QuickMath
from QuickMath import console
from rich.console import Console

console = Console()

def main():
	app = QuickMath()
	try:
		app.run()
	except KeyboardInterrupt:
		app.quickMath_exit()
	except EOFError:
		app.quickMath_exit()

if __name__ == "__main__":
	main()
