class Block:

    block_ids = {
        "clone:dirt": "brown",
        "clone:grass_block": "green",
        "clone:air": ""
    }
    xy={
        [0,0]:[20,20],
        [0,1]:[20,60],
        [1,0]:[60,20]
    }

    def draw_block(gridxy: str, block_id: str, canvas: Canvas):
        block = Block.block_ids[block_id]
        xy: list = Block.xy[gridxy]
        canvas.create_rectangle(xy[0], xy[1], 39, 39, fill=block, outline=block)