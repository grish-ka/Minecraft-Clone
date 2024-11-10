from tkinter import *
from Block import Block


class Player:
    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas
        self.mspeed: int
        self.coords = [0, 0]
        self.draw_player(self.coords[0], self.coords[1])

    def move_left(self):
        print("Pressed enter")

        Block.draw_block(x=self.coords[0], y=self.coords[1], block_id="clone:air", canvas=self.canvas)
        self.coords=[self.coords[0]+1, self.coords[1]]
        self.draw_player(self.coords[0], self.coords[1])


    def convert_coords_to_str(self, coords: list) -> str:
        return str(str(coords[0]) + "," + str(coords[1]))


    def move(self, root: Tk):
        canvas = self.canvas
        root.bind("<Right>", lambda event:self.move_left())
        root.bind("<KeyPress-Left>", lambda event: self.move_right())
        root.bind("<KeyPress-Up>", lambda event: self.move_up())
        root.bind("<KeyPress-Down>", lambda event:self.move_down())

    def draw_player(self, x, y):
        canvas = self.canvas
        xy = Block.get_xy(x, y)
        self.player: canvas.create_rectangle = canvas.create_rectangle(xy[0], xy[1], xy[0]+19, xy[1]+19,
                                                                       fill="blue", outline="blue")

    def move_down(self):
        Block.draw_block(x=self.coords[0], y=self.coords[1], block_id="clone:air", canvas=self.canvas)
        self.coords = [self.coords[0], self.coords[1] + 1]
        self.draw_player(self.coords[0], self.coords[1])

    def draw(self, root: Tk):
        self.move(root)

    def move_right(self):
        Block.draw_block(x=self.coords[0], y=self.coords[1], block_id="clone:air", canvas=self.canvas)
        self.coords = [self.coords[0]-1, self.coords[1]]
        self.draw_player(self.coords[0], self.coords[1])

    def move_up(self):
        Block.draw_block(x=self.coords[0], y=self.coords[1], block_id="clone:air", canvas=self.canvas)
        self.coords = [self.coords[0], self.coords[1]-1]
        self.draw_player(self.coords[0], self.coords[1])
