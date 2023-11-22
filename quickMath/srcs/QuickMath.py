from os import system
from time import sleep
from typing import Any
from rich import print as rprint
from rich.console import Console
from random import randint
from PlayerScore import PlayerScore

console = Console()


class QuickMath:
	def __init__(self):
		self.brun = True
		self.result = 0
		self.player_name = ""
		self.level = 0
		self.level_str = ""
		self.quiz = []
		self.score = 0
		self.quiz_count = 0
		self.player_score = None


	def get_level(self) -> int:
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		console.print("")
		console.print("1. Easy")
		console.print("2. Medium")
		console.print("3. Hard")
		console.print("4. Exit")
		console.print("")
		console.print("[bold yellow]Select a level: ", end="")
		data = str(input())
		if (data == "1" or data.lower() == "easy"):
			self.level = 10
			self.level_str = "Easy"
		elif (data == "2" or data.lower() == "medium"):
			self.level = 100
			self.level_str = "Medium"
		elif (data == "3" or data.lower() == "hard"):
			self.level = 1000
			self.level_str = "Hard"
		elif (data == "4" or data.lower() == "exit"):
			exit()
		else:
			return self.get_level()


	def get_player_name(self):
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		player_name = input("Player name: ")
		if (player_name == "" or player_name == None):
			self.get_player_name()
		else:
			self.player_name = player_name


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


	def validate_input_int(self, inp):
		self.validate_iscommand(inp)
		try:
			int(inp)
			return True
		except ValueError:
			return False


	def validate_input_str(self, inp) -> bool:
		try:
			str(inp)
			return True
		except ValueError:
			return False


	def print_quiz(self, header: str, quiz: str):
		console.print(header)
		console.print(quiz, end="")


	def multiply(self, num1, num2) -> None:
		self.print_score()
		self.print_quiz("[bold green]Multiply", f"{num1} * {num2} = ")
		result = input()
		if (self.validate_input_int(result)):
			result = int(result)
			self.validate_result(result, num1 * num2)
		else:
			self.multiply(num1, num2)
		return


	def add(self, num1, num2) -> None:
		self.print_score()
		self.print_quiz("[bold green]Add", f"{num1} + {num2} = ")
		result = input()
		if (self.validate_input_int(result)):
			result = int(result)
			self.validate_result(result, num1 + num2)
		else:
			self.multiply(num1, num2)
		return


	def sub(self, num1, num2) -> None:
		self.print_score()
		self.print_quiz("[bold green]Sub", f"{num1} - {num2} = ")
		result = input()
		if (self.validate_input_int(result)):
			result = int(result)
			self.validate_result(result, num1 - num2)
		else:
			self.multiply(num1, num2)
		return


	def print_score(self):
		system("clear")
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
		msg = f"[bold cyan1]No.[bold yellow]{self.quiz_count + 1} [bold cyan1]Mode: [bold yellow]{level} [bold cyan1]{self.player_name}: {color}{self.score}"
		console.print(msg)


	def set_player_score(self, title: str, mode: str) -> None:
		self.player_score = PlayerScore(title, mode)


	def quickMath_again(self):
		console.print("[bold yellow]You want to play again? [bold green]Y [bold yellow]or [bold red]N : ", end="")
		again = input()
		if (self.validate_input_str(again)):
			again = str(again)
		else:
			self.quickMath_again()
		if (again.lower() == 'y'):
			self.reset_score_and_run()
			self.brun = True
			self.get_level()
			return True
		elif (again.lower() == 'n'):
			self.quickMath_exit()
		else:
			self.quickMath_again()


	def quickMath_start(self) -> None:
		system("clear")
		while(self.brun and self.quiz_count < 10):
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
		system("clear")
		self.quiz_count -= 1
		self.print_score()
		if (self.quickMath_again()):
			self.quickMath_start()


	def quickMath_exit(self) -> None:
		system("clear")
		console.print("[bold bright_red]Bye bye~~~~~")
		sleep(1)
		system("clear")
		exit(0)


	def home(self) -> None:
		system("clear")
		console.print("[bold green]QuickMath[/bold green]")
		self.get_player_name()
		self.get_level()
		self.set_player_score(self.player_name.capitalize(), self.level_str)
		self.player_score.show_table()
		self.brun = True


	def reset_score_and_run(self) -> None:
		self.score = 0
		self.quiz_count = 0
		self.brun = False


	def run(self) -> None:
		self.home()
		self.quickMath_start()



