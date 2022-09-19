from src.figure import Figure


class Square(Figure):
    def __init__(self, side_1):
        super().__init__()
        self.name = 'square'
        self.side_1 = side_1
        self.perimeter = self.side_1 * 4
        self.area = self.side_1 ** 2




