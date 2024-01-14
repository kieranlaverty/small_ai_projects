
import board as b
def main():
    game = b.board()
    game.print()
    game.place_piece(3)
    game.place_piece(4)

    game.place_piece(4)
    game.place_piece(5)

    game.place_piece(5)
    game.place_piece(6)

    game.place_piece(5)
    game.place_piece(6)

    game.place_piece(5)
    game.place_piece(6)

    game.place_piece(6)
    game.place_piece(5)


    game.print()


if __name__ == "__main__":
    main()