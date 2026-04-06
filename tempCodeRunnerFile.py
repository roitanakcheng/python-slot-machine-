
                print (f"The number must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Enter a positive number please vro.")
                
    return amount

def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: 
                break
            else: 
                print("Enter a valid number of lines.")
        else: 
            print("Enter a line.")
    return lines

def main():

    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines