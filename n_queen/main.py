"""
This program solves the n-queen problem

"""

import queens as q

def main():
    board = q.queens(N = 9)
    board.solve()
    board.print(board.solution)


if __name__ == "__main__":
    main()