import random

MAX_LINES = 3 #z duzych liter gdy jest to stała wartosc i się nie zmieni
MAX_BET = 100 #maksymalna stawka
MIN_BET = 10 #minimalna

ROWS = 3  #ilosć wierszy w "maszynie"
COLS = 3 #ilosć kolumn


symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}
symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings , winnings_lines #zwracamy dwie wartości wygrana oraz info na których liniach wygrali

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols): #podkreśleniem oznaczamy zmienna która nie bedzie uzywana lub nie bedziemy sie odwoływać w petli
        column = []
        current_symbols = all_symbols[:] #kopiowanie listy umieszczamy dwukropek w naiwasie kwadratowym
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],  end= ' | ')
            else: 
                print(column[row], end = '')
        print()

def deposit(): #definujemy ilosć pieniedzy jaką ma gracz na poczatku rozgrywki
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greate than 0.')
        else: 
            print('Please enter a number.')
    return amount


def get_number_of_lines(): #definujemy pobieranie numeru lini od uzytkownika
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES)+ ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter the valid number of lines.')
        else: print('Please enter a number.')
    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else: 
            print('Please enter a number.')
    return amount
def spin(balance): # definujemy jedną rozgrywkę
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'you don not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break
    print(f'You are betting ${bet}on {lines} lines. Toatl bet is equal to: ${total_bet}')
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won${winnings}.')
    print(f'You won on lines: ', *winning_lines) #* operator rozpakowania? przekae kadą linie ze zwycieskiej lini do print 
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f'Current balance is: ${balance}')
        answer = input('Press enter to play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
    print('You left with${balance}')
main()
