# we will create a simple TIC TAC TOE game using python.

from mimetypes import init
import random

class TicTacToe:
    def __init__(self):
        self.board = []
    def create_board(self):
        for i in range(0,3):
            row = ['-','-','-']
            self.board.append(row)

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print('\n')

    def first_player(self):
        return random.randint(0,1)
    
    def mark_spot(self,row, column, player): 
        while True:
            if self.board[row-1][column-1]!='-':
                print("The Place is already taken. Please re enter the values of Row and Column")
                row,column = list(map(int, input().split()))
            else:
                break
        
        self.board[row-1][column-1] = player


    def switch_player(self,player):
        if(player==1):
            return 0
        else:
            return 1

    def player_win(self, player):
        #check for all the cases that can cause a win
        win = None
        n = len(self.board)

        #check case for rows only
        for row in self.board:
            for item in row:
                if(item==player):
                    win = True
                else:
                    win = False
                    break
            
            if win:
                return win
        
        # check for columns now
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i]!= player:
                    win = False
                    break
            
            if win:
                return win
            
        #check for diagonals now

        for i in range(n):
            win =  True
            if self.board[i][i] !=player:
                win = False
                break
                
        if win:
            return win
        
        #for second diagonal

        for i in range(n):
            win = True
            if self.board[i][n-1-i]!=player:
                win = False
                break    
        if win:
            return win
        return False
        

    def is_box_filled(self):
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True  

    def swap_player(self,player):
        return 'X' if player=="O" else "O"

    def start(self):
        self.create_board()
        player = "X" if self.first_player()==1 else "O"
        while True:
            print(f"Player {player} turn")
            self.print_board()

            row,col = list(map(int, input("Please enter the row and the column").split()))
                
            self.mark_spot(row,col,player)

            if self.player_win(player):
                print(f"Player {player} won!!")
                break
            
            if self.is_box_filled():
                print('Match Draw')
                break

            player = self.swap_player(player)




game = TicTacToe()

game.start()