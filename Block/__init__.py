from tkinter import *

class Block:

    def convert_coords_to_str(self, coords: list) -> str:
        return str(str(coords[0]) + "," + str(coords[1]))

    block_ids = {
        "clone:dirt": "brown",
        "clone:grass_block": "green",
        "clone:air": "white"
    }

    def get_xy( x, y):
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
        ["clone:dirt", "clone:grass_block", "clone:dirt"],
        ["clone:dirt", "clone:dirt", "clone:dirt"],
        ["clone:dirt", "clone:dirt", "clone:dirt"]
    ]

    def draw_block( x: int, y: int, block_id: str, canvas: Canvas):
        block = Block.block_ids[block_id]
        xy: tuple = Block.get_xy(x=x, y=y)
        canvas.create_rectangle(xy[0], xy[1], 39, 39, fill=block, outline=block)

    def draw_blocks(self, canvas: Canvas):
        for x in range(len(self.blocks)):
            for y in range(len(self.blocks)):
                print(self.blocks[x][y], "at", x, y)
                self.draw_block(x=x, y=y, block_id=self.blocks[x][y], canvas=canvas)


