from tkinter import *
from Block import Block


class Player:
    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas
        self.mspeed: int
        self.coords = [0, 0]
        self.xy = Block.xy[self.convert_coords_to_str(self.coords)]
        self.draw_player(self.coords)
        self.moves=[]

    def move_left(self):
        print("Pressed enter")

        Block.draw_block(gridxy=self.convert_coords_to_str(self.coords), block_id="clone:air", canvas=self.canvas)
        self.coords=[self.coords[0] + 1, self.coords[1]]
        self.draw_player(self.coords)
        self.moves.append(self.coords)


    def convert_coords_to_str(self, coords: list) -> str:
        return str(str(coords[0]) + "," + str(coords[1]))


    def move(self, root: Tk):
        canvas = self.canvas
        root.bind("<Return>", self.move_left())
        root.bind("<KeyPress-Down>", self.move_down())

    def draw_player(self, xy: list):
        canvas = self.canvas
        xy = Block.xy[self.convert_coords_to_str(xy)]
        self.player: canvas.create_rectangle = canvas.create_rectangle(xy[0], xy[1], 39, 39,
                                                                       fill="blue", outline="blue")

    def move_down(self):
        Block.draw_block(gridxy=self.convert_coords_to_str(self.coords), block_id="clone:air", canvas=self.canvas)
        self.coords = [self.coords[0], self.coords[1] + 1]
        self.draw_player(self.coords)
        self.moves.append(self.coords)

    def draw(self, root: Tk):
        self.move(root)
