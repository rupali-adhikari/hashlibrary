#Tictactoe game implementation in python
'''Here initially we wil be creating a board in which the game is to be played'''
Board = {'1': ' ','2': ' ','3': ' ',
         '4': ' ','5': ' ','6': ' ',
         '7': ' ','8': ' ','9': ' '}
board_key = []
for key in Board:
   board_key.append(key)
def printBoard(board):
    print('|' + board['1'] + '/' + board['2'] + '/' + board['3'] + '|')
    print('-------')
    print('|' + board['4'] + '/' + board['5'] + '/' + board['6'] + '|')
    print('-----')
    print('|' + board['7'] + '/' + board['8'] + '/' + board['9'] + '|')
    print('-------')


# Now we'll write the main function which has all the gameplay functionality.
def gameplay():
    turn = 'X'
    count = 0
    for g in range(10):
        printBoard(Board)
        print("Start to play,"+turn+".Move to place?")
        move=input()
        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("You already entered that number. choose another one")
            continue
#now lets check either player x or O has won. and following are the conditions according to which they can win.
# For every move after the 5th move
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':  # across the straight line
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['3'] == Board['5'] == Board['7'] != ' ':  # the diagonal
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':  # the diagonal
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['8'] == Board['5'] == Board['2'] != ' ':  # the vertical one
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['7'] == Board['6'] == Board['1'] != ' ':  # the vertical one
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
            elif Board['9'] == Board['6'] == Board['3'] != ' ':  # the vertical one
                printBoard(Board)
                print("\nGameOver.\n")
                print("***" + turn + "win.***")
                break
#now we will see if the above conditions are not true then a new condition will arise which is a tie condition
        if count == 9:
            print("\nGameOver\n")
            print("Tie Occurred")
#Now we will give change to the players accordingly
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
#Now we will ask the players if they want to restart the game by usung yes or no
        restart = input("Do you want to restart(y/n)")
        if restart == "y" or restart == "Y":
            for key in board_key:
                Board[key] = " "
            gameplay()

if __name__ == "__main__":
        gameplay()