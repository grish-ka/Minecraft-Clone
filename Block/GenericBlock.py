from Block import *
from tkinter import *

class GenericBlock:
    def __init__(self, x, y, blocktype: str, canvas: Canvas):
        Block.draw_block(x=x, y=y, block_id=blocktype, canvas=canvas)
