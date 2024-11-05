# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from tkinter import *

from CustomErrors import GridNotFound


class Block:

    block_ids = {
        "clone:dirt": "brown",
        "clone:grass_block": "green"
    }
    xy={
        "0,0":[20,20],
        "0,1":[20,60],
        "1,0":[60,20]
    }

    def draw_block(gridxy: str, block_id: str, canvas: Canvas):
        block = Block.block_ids[block_id]
        xy: list = Block.xy[gridxy]
        canvas.create_rectangle(xy[0], xy[1], 39, 39, fill=block, outline=block)


def main():
    tk = Tk()
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()

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
    Block.draw_block(gridxy="1,0", block_id="clone:dirt", canvas=canvas)


    while True:
        tk.update()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
