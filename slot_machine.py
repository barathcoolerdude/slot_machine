MAX_LINES=3
MIN_LINES=1

def deposit():
    while True:
        amount=input("Enter the amount you want to deposit: ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("deposit must be above 0. ")
        else:
            print("Enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter number of lines you want to bet on: ")
        if lines.isdigit():
            lines=int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print("Enter number betwwen (1 - " + str(MAX_LINES) + ") ")
        else:
            print("Enter a number")
    return lines
def main():
    balance=deposit()
    lines=get_number_of_lines()
main()