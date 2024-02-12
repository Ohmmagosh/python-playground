from rich.console import Console
from rich import print as rprint
from os import system
from time import sleep

console = Console()

class App:
	def __init__(self):
		pass


	def welcome_and_usage(self):
		console.print("[chartreuse1]Hello Eater")


	def msg_animate(self, msg: str, animate: str) -> None:
		try:
			for i in range(10):
				system('clear')
				t = msg + (animate * i)
				console.print(f"[yellow]{t}")
				sleep(0.2)
			system('clear')
		except KeyboardInterrupt:
			system('clear')
			exit()


	def exit(self):
		self.msg_animate("Bye", "~")


	def run(self):
		try:
			while(True):
				console.print("EATER LIST")
		except KeyboardInterrupt:
			self.exit()

