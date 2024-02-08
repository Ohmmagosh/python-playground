from time import sleep
from random import randint
from rich.console import Console
from rich.table import Table

profit = [0.03, 0.05, 0.1]
console = Console()

def main():
    total = 2500;
    count_percent_time=[0, 0, 0]
    
    table = Table(title="profit calclulator")

    table.add_column("No. ", justify="right", style="cyan", no_wrap=True)
    table.add_column("Monney", style="green3")
    table.add_column("Profit", justify="right", style="green")
    table.add_column("Random Profit", justify="right", style="yellow")




    count_time = 0
    while (total < 1000000):
        rand = randint(0, len(profit) - 1)
        profit_rand = total * profit[rand]
        count_percent_time[rand] += 1
        total += profit_rand
        count_time += 1;
        #console.print(f" No. {count_time} total {round(total,2)} profit_rand = {round(profit_rand,2)} rand = {int(profit[rand] * 100)} %")
        rand_percent_str =  f"{int(profit[rand] * 100)} %"
        table.add_row(str(count_time) , str(total), str(round(profit_rand,2)), rand_percent_str) 
    

    console.print(table)
    console.print(f" 3% = {count_percent_time[0]} 5% = {count_percent_time[1]} 10% = {count_percent_time[2]}")
    count_percent = count_percent_time[0] + count_percent_time[1] + count_percent_time[2]

    console.print(f" {count_percent_time[0]} + {count_percent_time[1]} + {count_percent_time[2]} = {count_percent}")



if __name__ == "__main__":
    main()
