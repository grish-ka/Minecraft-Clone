import unittest
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()


def draw_cloumns():
    for x in range(8):
        canvas.create_line(0,0,500,500)


canvas.create_line(0,0,500,500)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
