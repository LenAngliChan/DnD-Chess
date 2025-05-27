import arcade

from src.gui.window import ChessWindow


def start():

    window = ChessWindow()
    window.start_game()

    arcade.run()


if __name__ == '__main__':
    start()
