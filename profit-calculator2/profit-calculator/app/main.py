from time import sleep
from random import randint
from rich.console import Console
from rich.table import Table

from profit_calculator.profit_calculator.app import App

profit = [0.03, 0.05, 0.1]
console = Console()

def main():
    total = 2000
    count_percent_time=[0, 0, 0]

    table = Table(title="profit calclulator")

    table.add_column("No. ", justify="right", style="cyan", no_wrap=True)
    table.add_column("Monney", style="green3", justify="right")
    table.add_column("Profit $", justify="right", style="green")
    table.add_column("Profit %", justify="right", style="yellow1")

    count_time = 0
    while (total < 1000000):
        rand = randint(0, len(profit) - 1)
        profit_rand = total * profit[rand]
        count_percent_time[rand] += 1
        total += profit_rand
        count_time += 1
        rand_percent_str =  f"{round(int(profit[rand] * 100),2)} %"
        table.add_row(str(count_time) , str(round(total, 3)), str(round(profit_rand,2)), rand_percent_str)


    console.print(table)
    console.print(f" 3% = {count_percent_time[0]} 5% = {count_percent_time[1]} 10% = {count_percent_time[2]}")
    count_percent = count_percent_time[0] + count_percent_time[1] + count_percent_time[2]

    console.print(f" {count_percent_time[0]} + {count_percent_time[1]} + {count_percent_time[2]} = {count_percent}")



if __name__ == "__main__":
    App().run()

    # main()
