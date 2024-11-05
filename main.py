# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *


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

    draw_cloumns(chunk_size)
    draw_rows(chunk_size)

    while True:
        tk.update()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
