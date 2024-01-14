"""
This class hold a game of connect four with a board size of n


"""
class board():

    #constructor
    def __init__(self, n = 7) -> None:
        #size of board
        self.n = n

        #connect four board
        self.board = [[0 for _ in range(n)] for _ in range(n)]

        #bool that hold red or yellow player turn
        self.red_turn = True

        #hold the winner of the game to show the game is over
        self.winner = None

        #move counter
        self.move = 0

        return

    #places a piece given the column the piece was dropped in
    def place_piece(self, col):
        
        #if the game has a winner then state it in the console and who won
        if self.winner != None:
            print("game is over")
            
            if self.winner == 1:
                print("Red won")
            if self.winner == 2:
                print("Yellow won")

            return
        
        #loop to check where the piece be dropped
        for i in range(len(self.board)):

            #if the square in the column is empty
            if self.board[self.n - 1 - i][col] == 0:

                #if the turn is red place a one
                if self.red_turn:

                    #place a one in the square for red
                    self.board[self.n - 1 - i][col] = 1

                    #change turn
                    self.red_turn = not self.red_turn

                    #if there is a winner print the winner
                    if self.declare_winner(col, self.n - 1 - i, 1):
                        print("Red Wins")

                    break
                #if the turn is yellow place a 2
                else:
                    #place a 2 in the square for yellow
                    self.board[self.n - 1 - i][col] = 2

                    #change turn
                    self.red_turn = not self.red_turn

                    #if there is a winner print the winner
                    if self.declare_winner(col, self.n - 1 - i, 2):
                        print("Yellow wins")

                    break 
        
        self.move += 1

        return
    
    #declare a winner given the location of the last piece placed
    def declare_winner(self, col, row, color):
        
        #checks the three squares below to see if there is a col victory
        if self.n - row >= 3:
            for i in range(4):
                if row + i < self.n and self.board[row+i][col] != color:
                    break
                if row + i < self.n and i == 3:
                    self.winner = color
                    return True

        #check if there is a row win
        count = 0 #if count every equals four then there is a win
        for space in self.board[row]:
            if space == color:
                count += 1
                if count == 4:
                    self.winner = color
                    return True
            else:
                count = 0
        
        #check if there is 4 in a row diagnolly
        
        count1 = 0
        count2 = 0

        #get the starting row index that would go through the square in question
        b_SlantUp = row - col
        b_SlantDown = row + col
        

        for j in range(self.n):

            if b_SlantDown < self.n and b_SlantUp >= 0:
                print("ran")
                if self.board[b_SlantDown][j] == color:
                    count1 += 1
                    if count1 == 4:
                        self.winner = color
                        return True
                else:
                    count1 = 0

            if b_SlantUp < self.n and b_SlantUp >= 0:
                if self.board[b_SlantUp][j] == color:
                    
                    count2 += 1
                    if count2 == 4:
                        self.winner = color
                        return True
                else:
                    count2 = 0

            b_SlantDown = b_SlantDown - 1
            b_SlantUp = b_SlantUp + 1
        


        return False
    

    #function not finished
    #returns the best move of the current board
    def best_move(self):
        if self.red_turn:
            color = 1
        else:
            color = 2
        
        possible_move = board()
        moves = [None for _ in range(self.n)]
        
        for col in range(self.n):
            possible_move.set_board(self.board, color)


    def set_board(self, board, color) -> None:
        self.board = board

        self.n = len(board)

        if color == 1:
            self.red_turn = True
        else:
            self.red_turn = False
        
        return

    def print(self, board = None) -> None:
        if board == None:
            board = self.board
        
        for i in board:
            print(i)
        
        print("\n")
        return
            