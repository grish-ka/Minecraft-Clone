
class Grid:

    def draw_columns(canvas, size: int = 17, width: float = 20):
        length: float = size * width
        size = size + 1
        for x in range(size):
            canvas.create_line(x * width, 20, x * width, length)

    def draw_rows(canvas, size: int = 17, height: float = 20, width: float = 20):
        length: float = size * width
        size = size + 1
        for y in range(size):
            canvas.create_line(width, y * height, length, y * height)

    def draw_grid(self, canvas, size, height: float = 20, width: float = 20):
        self.draw_rows(canvas, size, height, width)
        self.draw_columns(canvas, size, width)
