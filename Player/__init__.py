from tkinter import *

class Player:
    def __init__(self, canvas):
        self.canvas: Canvas=canvas
        self.mspeed:int
        canvas.create_rectangle(20, 20, 39, 39, fill="blue", outline="blue")

    def move(self):
        self.mspeed=1
        canvas = self.canvas
