import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, side_1):
        super().__init__()
        self.side_1 = side_1
        self.name = 'circle'
        self.perimeter = round(2 * math.pi * side_1, 2)
        self.area = round(2 * math.pi * side_1**2, 2)


