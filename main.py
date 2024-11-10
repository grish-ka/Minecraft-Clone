# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from tkinter import *

from Grid import *
from CustomErrors import GridNotFound
from Block import Block
from Player import *







def main():
    tk = Tk()
    tk.title("Minecraft clone 0.1")
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()
    Block.draw_blocks(Block, canvas)


    def draw_columns(canvas, size: int = 17, width: float = 20):
        length: float = size * width
        size = size + 1
        for x in range(size):
            canvas.create_line(x * width, 20, x * width, length)

    def draw_rows(canvas, size: int = 17, height: float = 20, width: float = 20):
        length: float = size * width
        size = size + 1
        for y in range(size):
            canvas.create_line(width, y * height, length, y * height)

    chunk_size = 4

    n = random.randrange(0, 100000)
    if n == 100000:
        raise GridNotFound.GridNotFound("Grid Not Found")
    draw_columns(canvas=canvas, size=chunk_size)
    draw_rows(canvas=canvas, size=chunk_size)
    player = Player(canvas)


    while True:

        player.draw(tk)
        tk.update()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
