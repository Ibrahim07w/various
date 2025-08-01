import random

MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1
ROWS = COLS = 5
SYMBOLS = {'A':2, 'B':4, 'C':6, 'D':8}
VALUES = {'A':8, 'B':6, 'C':4, 'D':2}

def deposit():
    while True:
        amount = int(input('how much do you want to pay : '))
        if amount.isdigit():
            if int(amount) > 0:
                break
            else:
                print('please enter amount greater than 0')
        else:
            print('please enter numerical amount')
    return amount
def get_number_of_lines():
    while True:
        lines = int(input(f'enter number of lines (1-{MAX_LINES})'))
        if lines.isdigit():
            if 1 <= int(lines) <= MAX_LINES:
                break
            else:
                print(f'please enter lines bettween 1 and {MAX_LINES}')
        else:
            print('please enter numerical lines')
    return lines
def get_bet():
    while True:
        lines = int(input(f'enter number of lines ({MIN_BET}-{MAX_BET})'))
        if lines.isdigit():
            if MIN_BET <= int(lines) <= MAX_BET:
                break
            else:
                print(f'please enter lines bettween {MIN_BET} and {MAX_BET}')
        else:
            print('please enter numerical lines')
    return lines
def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()
def check_win(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print(f'too high bet please make it less than {balance}')
        else:
            break
    print(f'you are betting {bet} on {lines} lines with total {total}')
    slots = spin(ROWS, COLS, SYMBOLS)
    print_slot_machine(slots)
    winnings = check_win(slots, lines, bet, VALUES)
    print(f'you win {winnings}')
main()