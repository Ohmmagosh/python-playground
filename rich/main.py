from rich import print as rprint
from rich.console import Console
from time import sleep
from os import system as sys


console = Console()

def spinner():
    frame = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    while(True):
        sleep(0.5)
        #for i in frame:
        #    sleep(0.5)
        #    sys("clear")
        #    console.print(i, style="bold green")

def main():
    ob = { "hello": 123}
    rprint("hello")
    rprint(ob)
    console.print("HELLO", "World", style="bold green")
    #spinner()
    console.rule("[bold red]Chapter 2")
    with console.status("[bold green]Working...", spinner="dots"):
        spinner()

if __name__ == "__main__":
    main()
