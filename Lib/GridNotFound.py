class GridNotFound(Exception):
    def __init__(self, message: str="Grid Not Found"):
        self.message = message
