# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *


def main():
    tk = Tk()
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()

    def draw_cloumns(n: int = 16, width: float = 20, height: float = 400):
        length = n * width
        n=n+1
        for x in range(n):
            canvas.create_line(x*width, 500-height, x*width, height)

    def draw_rows(n: int = 16, height: float = 20,width: float = 20):
        length=n*width
        n=n+1
        for y in range(n):
            canvas.create_line(y*width, y*height, length, y*height)

    draw_cloumns()
    draw_rows()

    while True:
        tk.update()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
