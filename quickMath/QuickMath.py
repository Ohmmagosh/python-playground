from os import system
from time import sleep
from rich import print as rprint
from rich.console import Console
from random import randint

console = Console()


class QuickMath:
	def __init__(self):
		self.brun = True
		self.result = 0
		self.player_n = ""
		self.level = 0
		self.quiz = []
		self.score = 0
		self.quiz_count = 0


	def get_level(self) -> int:
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		console.print("1. Easy")
		console.print("2. Medium")
		console.print("3. Hard")
		console.print("4. Exit")
		console.print("")
		data = str(input("Select a level: "))
		if (data == "1" or data.lower() == "easy"):
			self.level = 10
		elif (data == "2" or data.lower() == "medium"):
			self.level = 100
		elif (data == "3" or data.lower() == "hard"):
			self.level = 1000
		elif (data == "4" or data.lower() == "exit"):
			exit()
		else:
			return self.get_level()


	def player_name(self):
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		player_name = input("Player name: ")
		if (player_name == "" or player_name == None):
			self.player_name()
		else:
			self.player_n = player_name


	def validate_iscommand(self, cmd):
		if (cmd.lower() == "exit"):
			exit()
		return


	def validate_result(self, result_input, cal):
		if(result_input == cal):
			self.score += 1
			console.print(":thumbs_up: [bold green]Correct")
		else:
			self.score -= 2
			console.print(f":pile_of_poo: [bold red]Incorrect result is {cal}")
		sleep(1)
		return


	def validate_input_quiz(self, inp):
		self.validate_iscommand(inp)
		try:
			int(inp)
			return True
		except ValueError:
			return False


	def multiply(self, num1, num2):
		system("clear")
		self.print_score()
		console.print("[bold green]Multiply")
		console.print(f"{num1} * {num2} = ", end="")
		result = input()
		if (self.validate_input_quiz(result)):
			result = int(result)
			self.validate_result(result, num1 * num2)
		else:
			self.multiply(num1, num2)
		return


	def add(self, num1, num2):
		system("clear")
		self.print_score()
		console.print("[bold green]Add")
		console.print(f"{num1} + {num2} = ", end="")
		result = input()
		if (self.validate_input_quiz(result)):
			result = int(result)
			self.validate_result(result, num1 + num2)
		else:
			self.multiply(num1, num2)
		return


	def sub(self, num1, num2):
		system("clear")
		self.print_score()
		console.print("[bold green]Sub")
		console.print(f"{num1} - {num2} = ", end="")
		result = input()
		if (self.validate_input_quiz(result)):
			result = int(result)
			self.validate_result(result, num1 - num2)
		else:
			self.multiply(num1, num2)
		return


	def print_score(self):
		if (self.level == 10):
			level = "Easy"
		elif (self.level == 100):
			level = "Medium"
		else:
			level = "Hard"
		if (self.score < 0):
			color = "[bold red]"
		else:
			color = "[bold green]"
		msg = f"[bold cyan1]No.[bold yellow]{self.quiz_count + 1} [bold cyan1]Mode: [bold yellow]{level} [bold cyan1]{self.player_n}: {color}{self.score}"
		console.print(msg)


	def quickMath_start(self):
		num1 = randint(1, self.level)
		num2 = randint(1, self.level)
		level = ["+", "-", "*"]
		rlevel = randint(0, len(level) - 1)
		match rlevel:
			case 0:
				self.add(num1, num2)
			case 1:
				self.sub(num1, num2)
			case 2:
				self.multiply(num1, num2)
		self.quiz_count += 1


	def quickMath_exit(self):
		system("clear")
		console.print("[bold bright_red]Bye bye~~~~~")
		sleep(1)
		system("clear")


	def home(self):
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		self.player_name()
		self.get_level()


	def run(self):
		system("clear")
		self.home()
		if (self.player_n != None and self.level != 0):
			self.brun = True
		while(self.brun and self.quiz_count < 10):
			self.quickMath_start()
		system("clear")
		self.quiz_count -= 1
		self.print_score()



