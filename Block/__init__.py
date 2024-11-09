from tkinter import *

class Block:

    def convert_coords_to_str(self, coords: list) -> str:
        return str(str(coords[0]) + "," + str(coords[1]))

    block_ids = {
        "clone:dirt": "brown",
        "clone:grass_block": "green",
        "clone:air": "white"
    }
    xy={
        "0,0":[20,20],
        "0,1":[20,60],
        "1,0":[60,20],
        "1,1": [60, 20],
        "2,1": [60, 20],
        "2,2": [60, 20],
        "2,3": [60, 20],
        "2,4": [60, 20],
        "2,5": [60, 20],
        "2,6": [60, 20],
        "2,8": [60, 20],
        "2,9": [60, 20],
        "2,10": [60, 20],
        "2,11": [60, 20],
        "2,12": [60, 20],
        "2,13": [60, 20],
        "2,14": [60, 20],
        "2,15": [60, 20],
        "2,16": [60, 20]

    }

    def __init__(self):
        for colum in range(16, 2):
            for row in range(16, 0):
                self.xy[self.convert_coords_to_str([colum, row])] = [60, 20]
                print(self.convert_coords_to_str([colum, row]))

        print(self.xy)

    def draw_block(gridxy: str, block_id: str, canvas: Canvas):
        block = Block.block_ids[block_id]
        xy: list = Block.xy[gridxy]
        canvas.create_rectangle(xy[0], xy[1], 39, 39, fill=block, outline=block)