from random import randrange
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

board[5] = 'X'

def printBoard():
    print(board[1] + '|' + board[2] + '|' + board[3], end='             ')
    print('1'+'|'+'2'+'|'+'3')
    print('-----' + '             ------')
    print(board[4] + '|' + board[5] + '|' + board[6], end='             ')
    print('4'+'|'+'5'+'|'+'6')
    print('-----' + '             ------')
    print(board[7] + '|' + board[8] + '|' + board[9], end='             ')
    print('7'+'|'+'8'+'|'+'9')
    print()


printBoard()

def rand_num():
    j = randrange(1, 10)
    if board[j] == ' ':
        board[j] = 'X'
        printBoard()
    else:
        rand_num()



while True:
    i = int(input("Box(1-9): "))
    if i == 10:
        printBoard()
        break
    if i<1 or i>9 or board[i]!=' ':
        continue
    else:
        board[i] = 'O'
        printBoard()
        rand_num()
        printBoard()
    if board[1]==board[2]==board[3]=='O' or board[4]==board[5]==board[6]=='O' or board[7]==board[8]==board[9] =='O' or\
   board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[3]==board[6]==board[9] =='O' or\
   board[1]==board[5]==board[9]=='O' or board[3]==board[5]==board[7]=='O':
     print ("CONGRATS, YOU WON!")
     break
    elif board[1]==board[2]==board[3]=='X' or board[4]==board[5]==board[6]=='X' or board[7]==board[8]==board[9]=='X' or\
   board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[3]==board[6]==board[9]=='X' or\
   board[1]==board[5]==board[9]=='X' or board[3]==board[5]==board[7]=='X':
        print("SORRY, COMPUTER WON!")
        break
    elif board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and \
        board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and \
        board[7]!=' ' and board[8]!=' ' and board[9]!=' ':
        print("OH, IT IS A TIE!")
        break
