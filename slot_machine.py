import random

MAX_LINE=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_Count in symbols.items():
        for _ in range(symbol_Count):
            all_symbols.append(symbol)

    columns=[]
    for col in range(cols):
        column=[]
        for row in range(rows):
            value = random.choice(all_symbols)
            print(col,row)

def get_deposit():
    while True:
        amount=input("Enter the amount you want to deposit:$ ")
        if amount.isdigit:
            amount=int(amount)
            if amount <= 0:
                print("Enter number greater than zero")
            else:
                break
        else:
            print("Enter a digit")
    return amount

def get_number_of_lines():
    while True:
        lines=input("enter number of lines you want to bet on: ")
        if lines.isdigit:
            lines=int(lines)
            if 1 <=lines <= MAX_LINE:
                break
            else:
                print("Enter number between (1 - "+str(MAX_LINE)+ ") ")
        else:
            print("Enter a digit")
    return lines


def get_bet():
    while True:
        amount=input("enter the amount you want to bet on each line:$ ")
        if amount.isdigit:
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"the amount must be between ${MIN_BET} - ${MAX_LINE} ")
        else:
            print("Enter a number")

    return amount

def main():
    balance=get_deposit()
    lines=get_number_of_lines()
    get_slot_machine_spin(3,3,symbol_count)
    while True:
        bet=get_bet()
        total_bet=lines * bet
        if total_bet < balance:
            break
        else:
            print(f"your balance is not enough, your balance is ${balance}")

    

main()