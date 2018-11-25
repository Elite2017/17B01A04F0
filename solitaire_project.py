board = [[' 0',' 1',' 2',' 3',' 4',' 5',' 6',' 7'],[' 1','  ','  ',' O',' O',' O','  ','  '],[' 2','  ','  ',' O',' O',' O','  ','  '],[' 3',' O',' O',' O',' O',' O',' O',' O'],[' 4',' O',' O',' O',' _',' O',' O',' O'],[' 5',' O',' O',' O',' O',' O',' O',' O'],[' 6','  ','  ',' O',' O',' O','  ','  '],[' 7','  ','  ',' O',' O',' O','  ','  ']]
def disp_board():
    for i in range(0, 8):
        for j in range(0, 8):
            print(board[i][j], end=" ")
        print('\n')
disp_board()
print('''BASIC INSTRUCTIONS:
        ENTER ROW NUMBER AND COLUMN NUMBER. THEN:
        PRESS U TO MOVE UP
        PRESS D TO MOVE DOWN
        PRESS R TO MOVE RIGHT
        PRESS L TO MOVE LEFT
        IF YOU ARE READY TO START THE GAME, PRESS "Y"
        IF YOU DON'T WANT TO CONTINUE THE GAME, PRESS "N"''')
ch = input("Enter Y/N :")
if ch == 'N':
    print("GAME ENDED")
elif ch == 'Y':
    #count = 31
    print("YOU CAN START THE GAME NOW")
    i = int(input("ENTER ROW(1,7):"))
    j = int(input("ENTER COLUMN(1,7):"))
    c = str(input("ENTER U / D / R / L :"))
    def values():
        p = int(input("ENTER ROW(1,7):"))
        q = int(input("ENTER COLUMN(1,7):"))
        cr = str(input("ENTER U / D / R / L :"))
        game(p, q, cr)
    def check():
        for i in range(1,8):
            for j in range(1,8):
                #if count == 0 :
                    #print("CONGRATULATIONS... YOU HAVE WON THE GAME")
                if board[i][j] == ' O':
                    if (board[i-1][j] == ' O' and board[i-2][j] == ' _') or (board[i+1][j] == ' O' and board[i+2][j] == ' _') or(board[i][j+1] == ' O' and board[i][j+2] == ' _') or (board[i][j-1] == ' O' and board[i][j-2] == ' _'):
                        print("NEXT MOVE")
                        values()
        print("OOPS! NO MORE POSSIBLE MOVES. THE GAME ENDS")
    def game(i,j,c):
        count = 31
        if c == 'L':
            if board[i][j] == " O" and board[i][j-1] == " O" and board[i][j-2] == " _":
                board[i][j] = ' _'
                board[i][j-1] = ' _'
                board[i][j-2] = ' O'
                disp_board()
                count = count - 1
                if count == 0:
                    print("CONGRATULATIONS... YOU HAVE WON THE GAME.")
                check()
            else:
                print("NOT A POSSIBLE MOVE. PLEASE GIVE ANOTHER VALUE.")
                values()
        elif c == 'R':
            if board[i][j] == " O" and board[i][j+1] == " O" and board[i][j+2] == " _":
                board[i][j] = ' _'
                board[i][j+1] = ' _'
                board[i][j+2] = ' O'
                disp_board()
                count = count - 1
                if count == 0:
                    print("CONGRATULATIONS... YOU HAVE WON THE GAME.")
                check()
            else:
                print("NOT A POSSIBLE MOVE. PLEASE GIVE ANOTHER VALUE.")
                values()
        elif c == 'U':
            if board[i][j] == " O" and board[i-1][j] == " O" and board[i-2][j] == " _":
                board[i][j] = ' _'
                board[i-1][j] = ' _'
                board[i-2][j] = ' O'
                disp_board()
                count = count - 1
                if count == 0:
                    print("CONGRATULATIONS... YOU HAVE WON THE GAME.")
                check()
            else:
                print("NOT A POSSIBLE MOVE. PLEASE GIVE ANOTHER VALUE.")
                values()
        elif c == 'D':
            if board[i][j] == " O" and board[i+1][j] == " O" and board[i+2][j] == " _":
                board[i][j] = ' _'
                board[i+1][j] = ' _'
                board[i+2][j] = ' O'
                disp_board()
                count = count - 1
                if count == 0:
                    print("CONGRATULATIONS... YOU HAVE WON THE GAME.") 
                check()
            else:
                print("NOT A POSSIBLE MOVE. PLEASE GIVR ANOTHER VALUE.")
                values()        
    game(i,j,c)
    print("oops")
