



class board():

    def __init__(self, n = 7) -> None:
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.red_turn = True
        self.winner = None

        self.move = 0

        return

    def place_piece(self, col):
        
        if self.winner != None:
            print("game is over")
            
            if self.winner == 1:
                print("Red won")
            if self.winner == 2:
                print("Yellow won")

            return
        
        for i in range(len(self.board)):
            if self.board[self.n - 1 - i][col] == 0:
                if self.red_turn:
                    self.board[self.n - 1 - i][col] = 1
                    self.red_turn = not self.red_turn
                    if self.declare_winner(col, self.n - 1 - i, 1):
                        print("Red Wins")
                    break
                else:
                    self.board[self.n - 1 - i][col] = 2
                    self.red_turn = not self.red_turn
                    if self.declare_winner(col, self.n - 1 - i, 2):
                        print("Yellow wins")
                    break 
        
        self.move += 1
        
        return
    
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
        
    def best_move(self):
        if self.red_turn:
            color = 1
        else:
            color = 2
        
        possible_move = board()

        for col in range(self.n):
            pass

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
            