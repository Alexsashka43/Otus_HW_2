import math

from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        super().__init__()
        self.name = 'triangle'
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.perimeter = self.side_1 + self.side_2 + self.side_3
        hp = self.perimeter / 2
        try:
            self.area = round(math.sqrt(hp * (hp - self.side_1) * (hp - self.side_2) * (hp - self.side_3)), 2)
        except Exception:
            print("Сумма двух сторон не должна быть меньше третьей.")





