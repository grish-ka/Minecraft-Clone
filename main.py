# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from tkinter import *

from CustomErrors import GridNotFound
from Block import Block
from Player import *







def main():
    tk = Tk()
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()
    Block()

    def draw_cloumns(size: int = 17, width: float = 20):
        length: float = size * width
        size = size + 1
        for x in range(size):
            canvas.create_line(x*width, 20, x*width, length)

    def draw_rows(size: int = 17, height: float = 20, width: float = 20):
        length: float = size * width
        size = size + 1
        for y in range(size):
            canvas.create_line(width, y*height, length, y*height)


    chunk_size = 17

    n = random.randrange(0, 100000)
    if n == 100000:
        raise GridNotFound.GridNotFound("Grid Not Found")
    draw_cloumns(chunk_size)
    draw_rows(chunk_size)
    Block.draw_block(gridxy="1,0", block_id="clone:grass_block", canvas=canvas)
    player = Player(canvas)


    while True:

        player.draw(tk)
        tk.update()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
