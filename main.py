# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

board_values = ['#','1','2','3','4','5','6','7','8','9']
guesses = []
def displayBoard():
    print(f'| {board_values[1]} | {board_values[2]} | {board_values[3]} |')
    print(f'| {board_values[4]} | {board_values[5]} | {board_values[6]} |')
    print(f'| {board_values[7]} | {board_values[8]} | {board_values[9]} |')

def verify_user_input():
    count = 0
    type = 'X'
    while len(guesses) < 10:
        choice = input('Select your position ')
        int_choice = int(choice)
        if int_choice < 10 and int_choice > 0 and board_values[int_choice] != 'X' and board_values[int_choice] != 'O':
# range function resulted in infinite loop ^
            guesses.append(choice)
            board_values[int_choice] = type
            displayBoard()
            count = count + 1
        else:
            print('Invalid input')

        if board_values[1] == board_values[2] == board_values[3]:
            print(f' {type} wins!')
            break
        elif board_values[4] == board_values[5] == board_values[6]:
            print(f' {type} wins!')
            break
        elif board_values[7] == board_values[8] == board_values[9]:
            print(f' {type} wins!')
            break
        elif board_values[1] == board_values[5] == board_values[9]:
            print(f' {type} wins!')
            break
        elif board_values[7] == board_values[5] == board_values[3]:
            print(f' {type} wins!')
            break
        elif board_values[1] == board_values[4] == board_values[7]:
            print(f' {type} wins!')
            break
        elif board_values[2] == board_values[5] == board_values[8]:
            print(f' {type} wins!')
            break
        elif board_values[3] == board_values[6] == board_values[9]:
            print(f' {type} wins!')
            break
        elif len(guesses) == 9:
            print('You tied!')
            break
        if count % 2 == 0:
            type = 'X'
        else:
            type = 'O'

def play_again():
    replay = input('Do you want to play again? (Y/N): ')
    if replay == 'y' or replay == 'Y':
# How do I restart my game? ^
        displayBoard()
        verify_user_input()
        play_again()
    elif replay == 'N' or replay == 'n':
        print('Thanks for playing!')
    else:
        print('Not a valid input')
        continue
# why is this continue not working? ^ pass works but not break and continue
displayBoard()
verify_user_input()
play_again()

