MAX_LINE=3


def get_deposit():
    while True:
        amount=input("Enter the amount you want to deposit")
        if amount.isdigit:
            amount=int(amount)
            if amount <= 0:
                print("enter number greater than zero")
            else:
                break
        else:
            print("enter a digit")
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the amount you want to deposit")
        if lines.isdigit:
            lines=int(lines)
            if 1 <=lines <= MAX_LINE:
                break
            else:
                print("ENTER number between 1 -"+str(MAX_LINE)+") ")
        else:
            print("Enter a digit")
    return lines

