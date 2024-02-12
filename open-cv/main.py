import pyautogui as pg
from rich.console import Console

console = Console()

def main():
	console.print("hello")
	img = pg.screenshot()
	img.save("test.png")
	# img.show()

if __name__ == "__main__":
	main()
