from time import sleep
from random import randint
from rich.console import Console
from rich.table import Table

from app import App

profit = [0.03, 0.05, 0.1]
console = Console()

def main():
    App().run()


if __name__ == "__main__":
    main()

