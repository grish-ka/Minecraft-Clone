from tkinter import *

import Grid


class Block:
    def convert_coords_to_str(self, coords: list) -> str:
        return str(str(coords[0]) + "," + str(coords[1]))

    block_ids = {
        "clone:dirt": "brown",
        "clone:grass_block": "green",
        "clone:air": "white"
    }

    def get_xy(x, y):
        start_x = 20
        start_y = 20
        width = 20
        return x * width + start_x, y * width + start_y

    def decon_xy(x, y):
        start_x = 20
        start_y = 20
        width = 20
        return x * width + start_x, y * width + start_y

    blocks = [
        ["clone:dirt", "clone:dirt", "clone:dirt"],
        ["clone:dirt", "clone:grass_block", "clone:dirt"],
        ["clone:dirt", "clone:dirt", "clone:dirt"]
    ]

    def draw_block(x: int, y: int, block_id: str, canvas: Canvas):
        block = Block.block_ids[block_id]
        xy = Block.get_xy(x, y)
        canvas.create_rectangle(xy[0], xy[1], xy[0]+19, xy[1]+19, fill=block, outline=block)

    def draw_blocks(self, canvas: Canvas):
        for x in range(len(self.blocks)):
            for y in range(len(self.blocks[x])):
                print(self.blocks[x][y], "at", x, y)
                self.draw_block(x, y, self.blocks[x][y], canvas)
                Grid.Grid.draw_grid(self=Grid.Grid, canvas=canvas, size=4)
