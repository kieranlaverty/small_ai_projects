

class queens():

    #constructor
    def __init__(self, N = 8) -> None:
        
        self.n = N
        self.board = [[None for _ in range(N)] for i in range(N)]
        self.solution = "no solution"
        self.solve()
        self.print(self.solution)
        
        return

    #check to see if a queen can be placed in 
    def is_legal(self, board, file, rank):
        
        #check if the rank is clear
        for i in range(file):
            if board[rank][i] != None:
                return False

        #check diagnals
        #check from square to top left
        for i, j in zip(range(rank, -1, -1), range(file, -1, -1)):
            if board[i][j] == "Q":
                return False
        
        #check from square to bottom left
        for i, j in zip(range(rank, self.n, 1), range(file, -1, -1)):
            if board[i][j] == "Q":
                return False


        return True
        
    #finds a solution
    def solve(self, board = None, file = 0):
        
        #default to unsolved
        if board == None:
            board = self.board
        
        #max number of queens placed therefore a solution has been found
        if file >= self.n:
            self.solution = board
            return True
        
        #cycle through each combinatation
        #j is the column number being checked
        for rank in range(self.n):
            
            #if the location is valid add the queen and move to next col
            if self.is_legal(board, file, rank):
                
                #input for the change
                board[rank][file] = "Q"

                
                #continue on the branch
                if self.solve(board, file + 1):
                    return True

                
                #reset
                board[rank][file] = None
            


        #no solution found
        return False


    def print(self, board = None) -> None:
        if board == None:
            board = self.board

        if board == "no solution":
            print("Please enter an n with a possible solution")
            return

        line = ""
        for i in self.board:
            for j in i:
                if j == None:
                    line += "_"
                else:
                    line += j
            print(line)
            line = ""
        print("\n")
        

        return

