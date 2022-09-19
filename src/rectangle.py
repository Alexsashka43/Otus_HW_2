from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_1, side_2):
        super().__init__()
        self.name = 'rectangle'
        self.side_1 = side_1
        self.side_2 = side_2
        self.perimeter = (self.side_1 + self.side_2) * 2
        self.area = self.side_1 * self.side_2


