import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLUMNS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows, columns, symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)


def deposit():
    while True:
        amount=input("what would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("must be higher than zero")
        else:
            print("please enter a number")
    return amount

def get_number_of_line():
     while True:
        lines=input("Enter the number of lines you want to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <=3:
                break
            else:
                print("lines must be between 1 - 3")
        else:
            print("please enter a number")
     return lines

def get_bet():
     while True:
        amount=input("what would you like to bet $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amonut must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number")
     return amount

def main():
    balance = deposit()
    lines=get_number_of_line()

    while True:
        bet=get_bet()
        total_bet= bet * lines
        if total_bet > balance:
            print(f"you do not have enough balance, your balance is ${balance}")

        else:
            break

    print(f"you are betting ${bet} on ${lines}. in total you are betting ${total_bet} ")
    print("bet: " + str(balance),", lines: "+str(lines))

main()
