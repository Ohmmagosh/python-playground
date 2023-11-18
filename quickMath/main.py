import random
import os
import time

def print_result(bresult: bool, msg: str):
    os.system("clear")
    if (bresult):
        print("Correct")
    else:
        print("Incorrect")
    print(msg)
    time.sleep(3)

def is_command(i) -> bool:
    if (i == "exit"):
        os.system("clear")
        return True
    return False

def validate_input(i) -> bool:
    if (is_command(i)):
        exit()
    try:
        int(i)
        return True
    except ValueError:
        return False
    
def get_input(msg: str) -> int:
    run = True
    while(run):
        data = input(msg)
        if (validate_input(data)):
            run = False
        else:
            os.system("clear")
    return int(data)
        
def main():
    os.system("clear")
    while (True):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        msg = f"{num1} + {num2} = "
        data = get_input(msg)
        if (num1 + num2 != data):
            print_result(False, f"{num1} + {num2} = {num1 + num2}")
        else:
            print_result(True, f"{num1} + {num2} = {num1 + num2}")
        os.system("clear")


if __name__ == "__main__":
    main()
