from tkinter import *
import Block

class Player:
    def __init__(self, canvas):
        self.canvas: Canvas = canvas
        self.mspeed:int
        self.coords = [0,0]
        self.xy = Block.Block.xy[self.coords]
        self.player: canvas.create_rectangle = canvas.create_rectangle(self.xy[0], self.xy[1], 39, 39,
                                                                       fill="blue", outline="blue")
        self.player.xy = self.xy

    def move_left(self):
        player = self.player
        player.xy = Block.Block.xy

    def move(self):
        canvas = self.canvas
        canvas.bind_all("<KeyPress-Left>", self.move_left())
